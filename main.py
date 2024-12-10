from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
    QDoubleSpinBox,
    QPushButton
)
from PyQt5 import uic
import sys

import numpy as np
import trimesh


from revolver import build_shape



class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("main.ui", self)
        self.show()

        # Find the double spin boxes
        self.len_1 = self.findChild(QDoubleSpinBox, "len_box_1")
        self.len_2 = self.findChild(QDoubleSpinBox, "len_box_2")
        self.len_3 = self.findChild(QDoubleSpinBox, "len_box_3")
        self.len_4 = self.findChild(QDoubleSpinBox, "len_box_4")

        self.rad_1 = self.findChild(QDoubleSpinBox, "rad_box_1")
        self.rad_2 = self.findChild(QDoubleSpinBox, "rad_box_2")
        self.rad_3 = self.findChild(QDoubleSpinBox, "rad_box_3")

        # Find buttons
        self.preview_button = self.findChild(QPushButton, "preview_button")
        self.preview_button.clicked.connect(self.preview_shape)

        self.export_button = self.findChild(QPushButton, "export_button")
        self.export_button.clicked.connect(self.export_file)

    

    def preview_shape(self):
        L1 = self.len_1.value()
        L2 = self.len_2.value()
        L3 = self.len_3.value()
        L4 = self.len_4.value()
        R1 = self.rad_1.value()
        R2 = self.rad_2.value()
        R3 = self.rad_3.value()

        self.vertices = np.array([
            [0, 0],  
            [R1, 0],  
            [R1, L1],  
            [R2, L3-L2],  
            [R2, L3],  
            [R3, L3],  
            [R3, L3+L4],  
            [0, L3+L4],
            [0, 0]
        ])

        self.built_shape = build_shape(self.vertices)

        self.built_shape.show()

    def export_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Mesh Files (*.stl *.obj *.step)"
        )
        if file_path:
            base_name, _ = file_path.rsplit('.', 1)

            # Export STL
            stl_path = f"{base_name}.stl"
            self.built_shape.export(stl_path)
            print(f"STL file saved at {stl_path}")

            # Export OBJ
            obj_path = f"{base_name}.obj"
            self.built_shape.export(obj_path)
            print(f"OBJ file saved at {obj_path}")

            # Export STEP (requires cadquery or similar library)
            try:
                from trimesh.exchange.export import export_mesh
                step_path = f"{base_name}.step"
                with open(step_path, 'wb') as step_file:
                    export_mesh(self.built_shape, file_obj=step_file, file_type='step')
                print(f"STEP file saved at {step_path}")
            except ImportError:
                print("STEP export requires additional libraries like cadquery.")
            except Exception as e:
                print(f"Failed to export STEP file: {e}")



app = QApplication(sys.argv)
window = UI()
app.exec_()
