import styles from "./index.module.scss";

import React from "react";

import { Field, Form, Formik, FormikActions, FormikProps } from "formik";
import { object, string } from "yup";

import { FormError, SubmitButton, TextField } from "../../components/form";

import { authService } from "../../services/AuthService";
import { Button } from "@blueprintjs/core";

export interface LoginFormProps {
	onSuccess: () => void;
}

export const LoginForm: React.FC<LoginFormProps> = (props) => {
	return (
		<Formik
			initialValues={{
				username: "",
				password: ""
			}}
			validationSchema={LoginRequestSchema}
			onSubmit={async (values: LoginRequest, actions: FormikActions<LoginRequest>) => {
				actions.setSubmitting(false);

				try {
					const isSuccess = await authService.login(values.username, values.password);
					if (isSuccess) {
						props.onSuccess();
					} else {
						actions.setStatus({ error: "An unexpected error has occurred" });
					}
				} catch (e: any) {
					if (e.cause.response) {
						// The request was made and the server responded with a status code
						// that falls out of the range of 2xx
						if (e.hasOwnProperty("cause") && e.cause.hasOwnProperty("response")) {
							console.log("EEEEEERRORRR: ", e.cause.response)
							actions.setStatus({ error: e.cause.response.data.nonFieldErrors[0] });
						}
					} else if (e.cause.request) {
						// The request was made but no response was received
						// `error.cause.request` is an instance of XMLHttpRequest in the
						// browser and an instance of http.ClientRequest in node.js
						actions.setStatus({ error: "Not connected to the internet or backend server is down." });
					} else {
						// Something happened in setting up the request that triggered an Error
						actions.setStatus({ error: "An unexpected error has occurred" });
					}
				}
			}}
		>
			{(formik: FormikProps<LoginRequest>) => (
				<Form className="space-y-4 md:space-y-6">
					{formik.status && formik.status.error && <FormError message={formik.status.error} />}
					<div>
						<label
							htmlFor="username"
							className="mb-2 block text-left text-sm font-medium">
							Your username
						</label>
						<Field
							id="username"
							className="focus:ring-primary-600 focus:border-primary-600 block w-full rounded-[20px] border border-gray-300 bg-gray-50 p-2.5 sm:text-sm"
							placeholder="username"
							type="username"
							name="username"
							labelError={true}
							required />
					</div>
					<div>
						<label
							htmlFor="password"
							className="mb-2 block text-left text-sm font-medium">
							Password
						</label>
						<Field
							id="password"
							className="focus:ring-primary-600 focus:border-primary-600 block w-full rounded-[20px] border border-gray-300 bg-gray-50 p-2.5 sm:text-sm"
							placeholder="********"
							type="password"
							name="password"
							labelError={true}
							required />
					</div>
					<button type="submit" className="w-full rounded-[20px] bg-[#542dbe] px-5 py-2.5 text-center text-sm font-medium text-white hover:border hover:border-[#542dbe] hover:bg-white hover:text-[#542dbe]">Sign in</button>
					{/* <Button
						className="w-full rounded-[20px] bg-[#542dbe] px-5 py-2.5 text-center text-sm font-medium text-white hover:border hover:border-[#542dbe] hover:bg-white hover:text-[#542dbe]"
						type="submit"
						text="Sign in"
						data-element-id="form-submit-button"
						// disabled={isSubmitting}
					/> */}
					{/* {formik.status && formik.status.error && <FormError message={formik.status.error} />}
					<TextField name="username" label="Username" labelError={true} />
					<TextField type="password" name="password" label="Password" labelError={true} />
					<SubmitButton /> */}
				</Form>
			)}
		</Formik>
	);
};

interface LoginRequest {
	username: string;
	password: string;
}

const LoginRequestSchema = object().shape({
	username: string()
		// .matches(/^[a-zA-Z0-9_]+$/, { message: "Username must contain only alphanumeric or underscore characters." })
		.required("Required"),
	password: string().required("Required")
});
