import React, { useMemo } from "react";
import { Callout, Intent } from "@blueprintjs/core";
import { LoginForm } from "./LoginForm";
import styles from "./index.module.scss";
import "./login.css";

export interface LoginDialogProps {
	isOpen: boolean;
	onSuccess: () => void;
}

export const LoginDialog: React.FC<LoginDialogProps> = (props) => (
	<div className="relative flex h-screen">
		<div className="hidden items-center justify-center bg-[#542dbe] text-center text-white md:flex md:w-[50%]">
			<img src="https://i.ibb.co/kKF0Wxp/DIA-LOGO-removebg-preview.png" alt="DIA-LOGO" />
		</div>
		<div className="w-full text-center md:w-[50%]">
			<div className="mx-auto flex flex-col items-center justify-center px-6 py-8 md:h-screen lg:py-0">
				<div className="w-full rounded-lg sm:max-w-md md:mt-0 xl:p-0">
					<div className="space-y-4 p-6 sm:p-8 md:space-y-6">
						<h1 className="text-xl font-bold leading-tight tracking-tight text-gray-500 md:text-2xl">Sign in to your account</h1>
						{/* <AuthStatusCallout /> */}
						<LoginForm onSuccess={props.onSuccess} />
					</div>
				</div>
			</div>
		</div>
	</div>
	// <Dialog
	//     className={classNames("bp3-dark", styles.dialog)}
	//     title="Login"
	//     icon="log-in"
	//     isOpen={props.isOpen}
	//     isCloseButtonShown={false}
	// >
	//     <div className={classNames(Classes.DIALOG_BODY, styles.body)} data-test-id="login-dialog">
	//         <AuthStatusCallout />
	//         {/* <LoginForm onSuccess={props.onSuccess} /> */}
	//     </div>
	// </Dialog>
);

const AuthStatusCallout: React.FC = () => {
	const params = useSearchParams();

	if (params.has("out")) {
		return <Callout className={styles.status} intent={Intent.SUCCESS} title="Logged Out" />;
	}
	if (params.has("error")) {
		return <Callout className={styles.status} intent={Intent.DANGER} title="Invalid Username or Password" />;
	}
	if (params.has("invalid")) {
		return (
			<Callout className={styles.status} intent={Intent.DANGER} title="Session Invalid - please login again" />
		);
	}
	if (params.has("time")) {
		return (
			<Callout className={styles.status} intent={Intent.DANGER} title="Session Timed Out - please login again" />
		);
	}

	return null;
};

export function useSearchParams(): URLSearchParams {
	return useMemo(() => new URLSearchParams(window.location.search), []);
}
