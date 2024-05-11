import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GLU import *
import pywavefront

def load_texture(texture_path):
    """텍스처 파일을 로드하여 OpenGL 텍스처로 설정합니다."""
    texture_surface = pygame.image.load(texture_path)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    # OBJ 파일 로드
    scene = pywavefront.Wavefront('/Users/caz/Desktop/NeRF 논문준비/3DModel2.obj', create_materials=True, collect_faces=True)
    
    # 텍스처 로드 및 OpenGL 설정
    textures = {}
    for material in scene.materials.values():
        if material.texture:
            tex_path = '/Users/caz/Desktop/NeRF 논문준비/3DModel/' + material.texture.file_name
            textures[material.name] = load_texture(tex_path)

    glEnable(GL_TEXTURE_2D)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # 여기에서 3D 렌더링을 수행하면서 텍스처를 적용
        for mesh in scene.mesh_list:
            for material in mesh.materials:
                if material in textures:
                    glBindTexture(GL_TEXTURE_2D, textures[material])
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3fv(mesh.vertices[vertex_i])
            glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()