import bpy
import bmesh

def Meshcalc(file_path):
   
    bpy.ops.import_scene.obj(filepath=file_path)

    # 
    obj = bpy.context.selected_objects[0]

    # mesh data calc
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.transform(obj.matrix_world)

    # 최대 및 최소 좌표를 계산합니다.
    min_coord = [float('inf'), float('inf'), float('inf')]
    max_coord = [-float('inf'), -float('inf'), -float('inf')]

    for v in bm.verts:
        for i in range(3):
            if v.co[i] < min_coord[i]:
                min_coord[i] = v.co[i]
            if v.co[i] > max_coord[i]:
                max_coord[i] = v.co[i]

    bm.free()  # bmesh clear

    # cube calc
    center = [(min_coord[i] + max_coord[i]) / 2 for i in range(3)]
    size = [(max_coord[i] - min_coord[i]) for i in range(3)]

    # cube gen
    bpy.ops.mesh.primitive_cube_add(size=1, location=center)
    cube = bpy.context.object
    cube.scale = [size[0]/2, size[1]/2, size[2]/2]

    # material
    material = bpy.data.materials.new(name="TransparentMaterial")
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs["Alpha"].default_value = 0.3
    material.blend_method = 'BLEND'
    cube.data.materials.append(material)

file_path = 'your_path.obj'
Meshcalc(file_path)
