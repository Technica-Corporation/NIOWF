import styles from "./index.module.scss";

import React, { useCallback, useEffect, useMemo, useState } from "react";
import { Spinner } from "@blueprintjs/core";

import { env, loginNextUrl } from "../../environment";
import { LoginDialog, RedirectDialog, useSearchParams } from "../../features/Login";
import { ConsentNotice } from "../../features/ConsentNotice";
import { UserAgreement } from "../../features/UserAgreement";
import { authService } from "../../services/AuthService";

export interface LoginPageProps {
    hideLogin: boolean;
    onConsentAcknowledged: () => void;
}

enum LoginState {
    Loading,
    Consent,
    UserAgreement,
    DisplayHello,
    Login,
    Redirect
}

export const LoginPage: React.FC<LoginPageProps> = (props) => {
    const consentOpts = useMemo(() => env().consentNotice, []);
    const agreementsOpts = useMemo(() => env().userAgreement, []);

    const nextUrl = useMemo(() => loginNextUrl(), []);

    const params = useSearchParams();
    const showLogin = useMemo(() => !props.hideLogin && !hasStatusParam(params), [params]);

    const [state, setState] = useState<LoginState>(showLogin ? LoginState.Login : LoginState.Loading);

    const redirectToDesktop = useCallback(() => {
        window.open(nextUrl, "_self");
        setState(LoginState.Redirect);
    }, []);

    useEffect(() => {
        const isConsentEnabled = consentOpts.isEnabled !== false && !hasStatusParam(params);
        setState(isConsentEnabled ? LoginState.Consent : LoginState.Login);
        authService
            .check()
            .then(() => {
                if (!props.hideLogin) redirectToDesktop();
                if (!isConsentEnabled) props.onConsentAcknowledged();
            })
            .catch(() => setState(isConsentEnabled ? LoginState.DisplayHello : LoginState.Login));
    }, []);

    useEffect(() => {
        let timeout: NodeJS.Timeout;
        if (state === LoginState.DisplayHello) {
            timeout = setTimeout(() => setState(LoginState.Login), 3000);
        }
        return () => clearTimeout(timeout);
    }, [state]);


    return (
        <div data-test-id="login-page" className={styles.root}>
            {state === LoginState.Loading && <Spinner className={styles.loadingSpinner} />}

            {/* <ConsentNotice
                opts={consentOpts}
                isOpen={state === LoginState.Consent}
                showUserAgreement={() => setState(LoginState.UserAgreement)}
                onAccept={() => {
                    setState(LoginState.DisplayHello);
                    props.onConsentAcknowledged();
                }}
            />

            <UserAgreement
                opts={agreementsOpts}
                isOpen={state === LoginState.UserAgreement}
                onClose={() => setState(LoginState.Consent)}
            /> */}

            {state === LoginState.DisplayHello && (
                // <Spinner className={styles.loadingSpinner} />
                <div style={{ display: "flex", justifyContent: "center",height:'100%' }}>
                         <img className={styles.logomain} src="/images/logomain.png" />
                    {/* <div className={styles.loadingSpinner} >{randomHelloMessage}</div> */}
                </div>
                
            )}

            <LoginDialog isOpen={state === LoginState.Login} onSuccess={redirectToDesktop} />

            <RedirectDialog isOpen={state === LoginState.Redirect} nextUrl={nextUrl} />
        </div>
    );
};

function hasStatusParam(params: URLSearchParams): boolean {
    return params.has("out") || params.has("error") || params.has("invalid") || params.has("time");
}
