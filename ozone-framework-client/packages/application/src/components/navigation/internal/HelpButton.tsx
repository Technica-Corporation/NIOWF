import React from "react";
import { Button } from "@blueprintjs/core";

import { useBehavior, useHotkey } from "../../../hooks";
import { Shortcuts } from "../../../shared/hotkeys";
import { mainStore } from "../../../stores/MainStore";

import { NavbarTooltip } from "./NavbarTooltip";
import { BsFillQuestionCircleFill } from "react-icons/bs";

const _HelpButton: React.FC = () => {
    const isVisible = useBehavior(mainStore.isHelpDialogVisible);

    useHotkey({ combo: Shortcuts.showHelp, onKeyDown: mainStore.showHelpDialog });

    return (
        <NavbarTooltip title="Help" shortcut={Shortcuts.showHelp} description="Show the Help window.">
            <Button
                minimal
                active={isVisible}
                onClick={mainStore.showHelpDialog}
                data-element-id="help-button"
            >
                <BsFillQuestionCircleFill/>
            </Button>
        </NavbarTooltip>
    );
};

export const HelpButton = React.memo(_HelpButton);
