import bpy

# ============ OBJETOS ============
destornillador = bpy.data.objects["destornillador "]
tapa = bpy.data.objects["tapa_trasera"]
brush = bpy.data.objects["brush"]

# ============ LIMPIAR KEYFRAMES ============
for obj in [destornillador, tapa, brush]:
    obj.animation_data_clear()

# ============ POSICIONES DEL DESTORNILLADOR ============
positions = [
    {"location": (-0.076605, 0.20105, 0.17586), "rotation": (95.864, -2468, -1103)},    # Pos 1
    {"location": (-0.076605, 0.20105, 0.062374), "rotation": (95.864, -2468, -1103)},   # Pos 2
    {"location": (-0.25098, -0.10243, 0.062374), "rotation": (95.864, -2457.9, -1281)}, # Pos 3 (actualizada)
    {"location": (-0.25098, -0.10243, 0.17586), "rotation": (95.864, -2468, -1281)}     # Pos 4 (actualizada)
]

frame = 1
rotation_duration = 20
movement_duration = 10

# ============ ANIMACIÓN DESTORNILLADOR - PRIMERA FASE ============
for pos in positions:
    loc = pos["location"]
    rot = [r * 3.1416 / 180 for r in pos["rotation"]]  # convertir a radianes

    destornillador.location = loc
    destornillador.rotation_euler = rot
    destornillador.keyframe_insert(data_path="location", frame=frame)
    destornillador.keyframe_insert(data_path="location", frame=frame + rotation_duration)
    destornillador.keyframe_insert(data_path="rotation_euler", frame=frame)

    # Solo rota en eje Y
    destornillador.rotation_euler[1] += (360 * 3.1416 / 180)
    destornillador.keyframe_insert(data_path="rotation_euler", frame=frame + rotation_duration)

    frame += rotation_duration + movement_duration

# ============ TAPA: RETIRO ============
tapa_start = frame
tapa.location = (-0.22844, 0.082855, 0.1153)
tapa.keyframe_insert(data_path="location", frame=tapa_start)

tapa.location.x -= 0.2
tapa.keyframe_insert(data_path="location", frame=tapa_start + 30)

# ============ BRUSH: MOVIMIENTO DE LIMPIEZA ============
brush_start = tapa_start + 31
z_top = 0.24208
z_bottom = 0.04208

brush.location = (-0.3141, -0.066377, z_top)
brush.keyframe_insert(data_path="location", frame=brush_start)

# Baja
brush.location.z = z_bottom
brush.keyframe_insert(data_path="location", frame=brush_start + 20)

# Sube
brush.location.z = z_top
brush.keyframe_insert(data_path="location", frame=brush_start + 40)

# Baja 2
brush.location.z = z_bottom
brush.keyframe_insert(data_path="location", frame=brush_start + 60)

# Sube 2
brush.location.z = z_top
brush.keyframe_insert(data_path="location", frame=brush_start + 80)

# ============ TAPA: REGRESO A SU POSICIÓN ORIGINAL ============
tapa_return_start = brush_start + 81
tapa.location.x = -0.42844
tapa.keyframe_insert(data_path="location", frame=tapa_return_start)

tapa.location.x = -0.22844
tapa.keyframe_insert(data_path="location", frame=tapa_return_start + 30)

# ============ DESTORNILLADOR: REPITE EN REVERSA ============
reverse_positions = list(reversed(positions))
frame = tapa_return_start + 61

for pos in reverse_positions:
    loc = pos["location"]
    rot = [r * 3.1416 / 180 for r in pos["rotation"]]

    destornillador.location = loc
    destornillador.rotation_euler = rot
    destornillador.keyframe_insert(data_path="location", frame=frame)
    destornillador.keyframe_insert(data_path="location", frame=frame + rotation_duration)
    destornillador.keyframe_insert(data_path="rotation_euler", frame=frame)

    destornillador.rotation_euler[1] += (360 * 3.1416 / 180)  # solo eje Y
    destornillador.keyframe_insert(data_path="rotation_euler", frame=frame + rotation_duration)

    frame += rotation_duration + movement_duration

# ============ BRUSH: TRASLADO A NUEVA POSICIÓN ============
brush_final_start = frame + 1
brush.keyframe_insert(data_path="location", frame=brush_final_start)

brush.location = (-0.36553, -0.027984, 0.234695)
brush.keyframe_insert(data_path="location", frame=brush_final_start + 20)

# ============ BRUSH: MOVIMIENTO DE LIMPIEZA EN NUEVA UBICACIÓN ============
brush_new_start = brush_final_start + 21
z_top_new = 0.234695
z_bottom_new = 0.014695

brush.location = (-0.36553, -0.027984, z_top_new)
brush.keyframe_insert(data_path="location", frame=brush_new_start)

# Baja
brush.location.z = z_bottom_new
brush.keyframe_insert(data_path="location", frame=brush_new_start + 20)

# Sube
brush.location.z = z_top_new
brush.keyframe_insert(data_path="location", frame=brush_new_start + 40)

# Baja 2
brush.location.z = z_bottom_new
brush.keyframe_insert(data_path="location", frame=brush_new_start + 60)

# Sube 2
brush.location.z = z_top_new
brush.keyframe_insert(data_path="location", frame=brush_new_start + 80)
s