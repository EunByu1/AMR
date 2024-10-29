import omni.usd
import omni.ui as ui
from omni.isaac.ui.element_wrappers import CollapsableFrame
from omni.isaac.ui.element_wrappers.core_connectors import LoadButton
from omni.isaac.core.world import World
from pxr import UsdPhysics, PhysxSchema
from omni.isaac.ui.ui_utils import get_style



class UIBuilder:
    def __init__(self):
        # UI elements created using a UIElementWrapper instance
        self.wrapped_ui_elements = []
        
        
    # ======================= ui =======================
    def build_ui(self):
        """
        Build a custom UI tool to run your extension.
        This function will be called any time the UI window is closed and reopened.
        """
        
        # [Setting] Controller
        # Toggle_1: Information
        info_frame = CollapsableFrame("Information", collapsed=False)
        
        with info_frame:
            with ui.VStack(style=get_style(), gspacing=5, height=0):
                ui.Label("Overview")
                # Create a frame with a custom background color for the description content
                with ui.ZStack(height=40):  # Set the height as needed
                        # Background frame
                    ui.Rectangle(style={"background_color": 0x2FFFFFFF})  # Dark gray background with full opacity
                        
                        # Text Label inside the background frame
                    description_text = (
                            "Establishment of Nvidia Isaac Sim digital twin for AMR-based port logistics automation"
                    )
                    self._description_label = ui.Label(description_text)
                    self._description_label.word_wrap = True
                
        # Toggle_2: Controller
        controller_frame = CollapsableFrame("Controller", collapsed=False)
        
        with controller_frame:
            with ui.VStack(style=get_style(), gspacing=5, height=0):
                self._load_btn = LoadButton(
                    "Load Button", "Load", setup_scene_fn=self._setup_scene)
                
                
                # [option] 시뮬레이션 환경 업데이트 속도 지정
                # self._load_btn.set_world_settings(physics_dt=1 / 60.0, rendering_dt=1 / 60.0)
                self.wrapped_ui_elements.append(self._load_btn)
    
    # ============================================================================
      
                
                
    # ======================= yard 호출 및 물리 scene 적용 =======================
    def _setup_scene(slef):
        """
        This function is attached to the Load Button as the setup_scene_fn callback.
        On pressing the Load Button, a new instance of World() is created and then this function is called.
        """
        
        # Instantiate the World object: 월드 객체 인스턴스화
        world = World.instance()
        
        # USD File Path 
        usd_path = r"C:/Users/kime/Desktop/Yard/Yard_Layout_Design_Ground_sky(700x1100)_v7.3usd.usd"
        
        # Open the USD file as the current stage, replacing any existing stage contents
        omni.usd.get_context().open_stage(usd_path)
        
        # PhysicsScene
        stage = omni.usd.get_context().get_stage()
        
        if not stage.GetPrimAtPath("/World/physicsScene"):
            UsdPhysics.Scene.Define(stage, "/World/physicsScene")

        # [PhysX error solution: Illegal BroadPhaseUpdateData]Simulation 관리를 위한 PhysxScene 설정 추가
        physx_scene = PhysxSchema.PhysxScene.Define(stage, "/World/physicsScene")
        physx_scene.GetGravityDirectionAttr().Set((0.0, 0.0, -1.0))  # 중력 방향 설정
        physx_scene.GetGravityMagnitudeAttr().Set(981.0)             # 중력 크기 설정
    
        print("USD file fully loaded as the current stage.")
    # ============================================================================
    
    
    
    # ======================= Callback =======================
    def on_menu_callback(self):
        """Callback for when the UI is opened from the toolbar.
        This is called directly after build_ui().
        """
        pass
    # ============================================================================
