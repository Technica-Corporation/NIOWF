import React from "react";
import { AnchorButton } from "@blueprintjs/core";
import { dashboardStore } from "../../../stores/DashboardStore";
import { FaSave } from "react-icons/fa";

export interface SaveDashboardButtonProps {
    isStoreOpen: boolean;
}

const _SaveDashboardButton: React.FC<SaveDashboardButtonProps> = ({ isStoreOpen }) => (
    <AnchorButton
        data-element-id="save-dashboard"
        minimal
        onClick={dashboardStore.saveCurrentDashboard}
        disabled={isStoreOpen}
    >
        <FaSave/>
    </AnchorButton>
);

export const SaveDashboardButton = React.memo(_SaveDashboardButton);
