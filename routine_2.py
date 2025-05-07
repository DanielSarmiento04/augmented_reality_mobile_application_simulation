import bpy
from mathutils import Euler

brush = bpy.data.objects['brush']
brush.animation_data_clear()

# ========== RUTINA 1: Limpieza superior (EJE X) ==========
rotation_sup = Euler((-20.146 * 3.1416 / 180, 83.894 * 3.1416 / 180, 69.664 * 3.1416 / 180), 'XYZ')
start_loc_sup = (-0.21821, -0.19934, 0.28185)
end_loc_sup = (0.28809, -0.19934, 0.28185)

frame = 1
for i in range(2):  # Repetir ida y vuelta
    brush.location = start_loc_sup
    brush.rotation_euler = rotation_sup
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = end_loc_sup
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = start_loc_sup
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

# ========== RUTINA 2: Limpieza lateral VERTICAL (EJE Z) ==========
rotation_lat_v = Euler((-84.264 * 3.1416 / 180, -4.0246 * 3.1416 / 180, -0.47601 * 3.1416 / 180), 'XYZ')
start_loc_lat_v = (-0.29992, -0.19934, 0.20982)
end_loc_lat_v = (-0.29992, -0.19934, 0.01484)

for i in range(2):
    brush.location = start_loc_lat_v
    brush.rotation_euler = rotation_lat_v
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = end_loc_lat_v
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = start_loc_lat_v
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

# ========== RUTINA 3: Limpieza lateral HORIZONTAL (EJE X) ==========
rotation_lat_h = Euler((-162.49 * 3.1416 / 180, -2.4808 * 3.1416 / 180, 91.96 * 3.1416 / 180), 'XYZ')
start_loc_lat_h = (-0.21035, -0.21843, 0.26833)
end_loc_lat_h = (0.33338, -0.21843, 0.26833)

for i in range(2):  # Dos repeticiones completas (ida y vuelta)
    brush.location = start_loc_lat_h
    brush.rotation_euler = rotation_lat_h
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = end_loc_lat_h
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = start_loc_lat_h
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)
# ========== RUTINA 4: Limpieza lateral opuesta (EJE X) ==========
rotation_lat_op = Euler((-192.49 * 3.1416 / 180, 2.5192 * 3.1416 / 180, -88.0398 * 3.1416 / 180), 'XYZ')
start_loc_lat_op = (-0.20035, 0.130968, 0.28833)
end_loc_lat_op = (0.251757, 0.130968, 0.28833)

# Inicia en frame 181
frame = 181
for i in range(2):  # Dos repeticiones (ida y vuelta)
    brush.location = start_loc_lat_op
    brush.rotation_euler = rotation_lat_op
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = end_loc_lat_op
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = start_loc_lat_op
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)
    # ===================== RUTINA 5: Limpieza tapa delantera =====================
rotation_front = Euler((-190.946 * 3.1416 / 180, -2.67543 * 3.1416 / 180, -192.964 * 3.1416 / 180), 'XYZ')
start_loc_front = (0.315954, 0.044029, 0.23674)
end_loc_front = (0.315954, -0.13811, 0.23674)

for i in range(2):  # Dos repeticiones (ida y vuelta)
    brush.location = start_loc_front
    brush.rotation_euler = rotation_front
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = end_loc_front
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)

    frame += 15
    brush.location = start_loc_front
    brush.keyframe_insert(data_path='location', frame=frame)
    brush.keyframe_insert(data_path='rotation_euler', frame=frame)