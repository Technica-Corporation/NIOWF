import React, { useCallback } from "react";
import { Button } from "@blueprintjs/core";

import { useHotkey } from "../../../hooks";
import { Shortcuts } from "../../../shared/hotkeys";

import { mainStore } from "../../../stores/MainStore";
import { NavbarTooltip } from "./NavbarTooltip";
import { FiShoppingCart } from "react-icons/fi";

const _StoreButton: React.FC = () => {
    const toggleStore = () => {
        mainStore.toggleStore();
    };

    useHotkey({ combo: Shortcuts.showStore, onKeyDown: toggleStore });

    return (
        <NavbarTooltip title="Marketplace" shortcut={Shortcuts.showStore} description="Open Marketplace">
            <Button minimal onClick={toggleStore} data-element-id="store-button">
                <FiShoppingCart />
            </Button>
        </NavbarTooltip>
    );
};

export const StoreButton = React.memo(_StoreButton);
