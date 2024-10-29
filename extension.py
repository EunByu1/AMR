import omni.ext
import omni.ui as ui
import omni.kit.commands
import omni.physx as _physx
from omni.isaac.ui.element_wrappers import ScrollingWindow
from omni.isaac.ui.menu import MenuItemDescription
from omni.kit.menu.utils import add_menu_items, remove_menu_items

from .ui_builder import UIBuilder
from .global_variables import EXTENSION_TITLE



class PortlogisticsautomationExtension(omni.ext.IExt):
    
    # ======================= setup =======================
    def on_startup(self, ext_id):
        """Initialize extension and UI elements"""
        print("[DEBUG] on_startup called")
        self.ext_id = ext_id
        self._usd_context = omni.usd.get_context()
        
        # Build Window
        self._window = ScrollingWindow(
            title=EXTENSION_TITLE, width=350, height=185, visible=True, dockPreference=ui.DockPreference.LEFT_BOTTOM
        )
        
        # Filled in with User Functions
        self.ui_builder = UIBuilder()
        
        # Events
        self._usd_context = omni.usd.get_context()
        self._physxIFace = _physx.acquire_physx_interface()
        
        # Directly build the UI immediately after creating the window
        self._build_ui() 
    # ============================================================================



    # ======================= ui_builder 호출 =======================
    def _build_ui(self):
        with self._window.frame:
            with ui.VStack(spacing=5, height=0):
                self._build_extension_ui()
    # ============================================================================

                       
                       
    # ======================= shutdown =======================
    def on_shutdown(self):
        print("[PORTLOGISTICSAUTOMATION] PORTLOGISTICSAUTOMATION shutdown")
    # ============================================================================



    # ======================= menu_callback =======================
    def _menu_callback(self):
        self._window.visible = not self._window.visible
        self.ui_builder.on_menu_callback()
    # ============================================================================

    
    
    # ======================= ui_builder 호출 =======================
    def _build_extension_ui(self):
        # Call user function for building UI
        self.ui_builder.build_ui()
    # ============================================================================
