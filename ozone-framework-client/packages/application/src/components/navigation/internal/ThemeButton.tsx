import React from "react";
import { Button } from "@blueprintjs/core";

import { useHotkey } from "../../../hooks";
import { Shortcuts } from "../../../shared/hotkeys";
import { mainStore } from "../../../stores/MainStore";

import { NavbarTooltip } from "./NavbarTooltip";
import { BsFillMoonFill } from "react-icons/bs";

const _ThemeButton: React.FC = () => {
    useHotkey({ combo: Shortcuts.toggleTheme, onKeyDown: mainStore.toggleTheme });

    return (
        <NavbarTooltip
            title="Theme"
            shortcut={Shortcuts.toggleTheme}
            description="Toggle between light and dark themes."
        >
            <Button minimal onClick={mainStore.toggleTheme} data-element-id="theme-button">
                <BsFillMoonFill/>
            </Button>
        </NavbarTooltip>
    );
};

export const ThemeButton = React.memo(_ThemeButton);
