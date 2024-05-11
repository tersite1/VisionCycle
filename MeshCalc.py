import bpy
import bmesh

def Meshcalc(file_path):
    # OBJ 파일을 임포트합니다.
    bpy.ops.import_scene.obj(filepath=file_path)

    # 활성 오브젝트를 가져옵니다.
    obj = bpy.context.selected_objects[0]

    # bmesh를 사용하여 메쉬 데이터를 계산합니다.
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

    bm.free()  # bmesh 클리어

    # 큐브의 중심과 크기 계산
    center = [(min_coord[i] + max_coord[i]) / 2 for i in range(3)]
    size = [(max_coord[i] - min_coord[i]) for i in range(3)]

    # 큐브 생성
    bpy.ops.mesh.primitive_cube_add(size=1, location=center)
    cube = bpy.context.object
    cube.scale = [size[0]/2, size[1]/2, size[2]/2]

    # 투명한 재질 설정
    material = bpy.data.materials.new(name="TransparentMaterial")
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs["Alpha"].default_value = 0.3
    material.blend_method = 'BLEND'
    cube.data.materials.append(material)

# 이제 Meshcalc 함수를 사용하여 작업을 수행할 수 있습니다.
file_path = '/Users/caz/Downloads/3DModel/OBJ/3DModel.obj'
Meshcalc(file_path)
