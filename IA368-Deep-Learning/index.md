# Descripcion de proyecto
El presente proyecto tiene como objetivo desarrollar un sistema de control Pan-Tilt para la cabeza de un robot social, orientado al seguimiento dinámico de personas mediante técnicas de visión computacional. La propuesta busca mejorar la capacidad del robot para mantener contacto visual y orientar su atención hacia uno o varios usuarios durante la interacción, incrementando así la naturalidad y el realismo comunicativo. Dado que el procesamiento se realizará en plataformas de bajo costo computacional, como Raspberry Pi o Jetson Nano, se evaluarán estrategias eficientes de detección y seguimiento que equilibren precisión y rendimiento, permitiendo una respuesta fluida y adaptable al contexto conversacional.

A partir de este módulo de seguimiento visual, el sistema podrá identificar patrones comunes en las condiciones de interacción, facilitando el desarrollo de conversaciones más personalizadas según la posición y comportamiento del usuario. En una etapa futura, se plantea ampliar las capacidades del modelo hacia el reconocimiento de características personales, como prendas o accesorios, para enriquecer el nivel de contextualización sin necesidad de capturar información del entorno físico. De esta forma, el proyecto sienta las bases para una interacción más empática, atenta y socialmente coherente entre humanos y robots.





Podemos entrenar un modelo con pocas imagenes de personas para reconocer el rostro de ellas, usando un VLM de las que ya aprendimos usando en la [Aula 7](../Aula_7/)


```markdown
┌───────────────────────────────────────────────────────────────┐
│                   🔹 SISTEMA COGNITIVO MULTIMODAL 🔹          │
│     (Atención Visual, Reconocimiento de Contexto y Diálogo)   │
└───────────────────────────────────────────────────────────────┘
                             │
                             ▼
            ┌──────────────────────────────┐
            │        CAPTURA SENSORIAL     │
            │ ─────────────────────────────│
            │ 📷 Cámara RGB                │
            │ 🎙️ Micrófono (entrada voz)   │
            └──────────────────────────────┘
            │                          │
            ▼                          ▼
    ┌────────────────────┐      ┌────────────────────────┐
    │ Módulo de Visión   │      │ Módulo de Voz          │
    │ ───────────────────│      │ ───────────────────────│
    │ • Detección facial │      │ • Speech-to-Text (STT) │
    │ • Estimación pose  │      │   (ej. Whisper)        │
    │ • Contexto físico  │      │ • Limpieza semántica   │
    └────────────────────┘      └────────────────────────┘
            │                          │
            ▼                          ▼
┌──────────────────────────────┐    ┌──────────────────────────────┐
│ Embedding Visual (VLM)       │    │ Embedding Textual (LLM/STT)  │
│ ─────────────────────────────│    │ ─────────────────────────────│
│ • Modelo: CLIP / SigLIP      │    │ • Modelo: BERT / CLIP-Text   │
│ • Extrae vector semántico    │    │ • Extrae vector contextual   │
└──────────────────────────────┘    └──────────────────────────────┘
            │                          │
            └──────────────┬───────────┘
                           ▼   
            ┌───────────────────────────────────┐
            │     ALINEAMIENTO MULTIMODAL       │
            │ ───────────────────────────────── │
            │ • Proyecciones lineales           │
            │ • Contrastive Loss (tipo CLIP)    │
            │ • Espacio semántico común         │
            │   → persona con muletas ↔ imagen  │
            └───────────────────────────────────┘
                            │
                            ▼
    ┌─────────────────────────────────────────────┐
    │       MÓDULO DE RAZONAMIENTO Y MEMORIA      │
    │ ─────────────────────────────────────────── │
    │ • LLM (chatbot) con memoria contextual      │
    │ • Record de interacción (texto + embeddings)│
    │ • Adaptación a usuario: tono, ritmo, tema   │
    └─────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│        MÓDULO DE CONTROL PAN–TILT Y ACCIONES (v2 – DXL)      │
│──────────────────────────────────────────────────────────────│
│ • Bus: U2D2 Power Hub Board  → RS-485 (Protocol 2.0)         │
│ • Actuadores: 2× Dynamixel XH540-W270-R (Pan = ID:1, Tilt:2) │
│ • Juntas: 2 GDL (pan/tilt) con límites angulares configurados│
│ • Control de movimiento:                                     │
│    – Generador de trayectorias (min-jerk / trapezoidal)      │
│    – Perfil de velocidad/aceleración (Profile Vel/Acc)       │
│    – SyncWrite para comandos simultáneos (pan+tilt)          │
│    – BulkRead para feedback (pos, vel, carga, temp)          │
│ • Modo de control: Position (con Current/Torque limit)       │
│ • Calibración/Homing: offset inicial + soft limits por junta │
│ • Seguridad: watchdog, torque enable/disable, temp thresholds│
│ • Resultado: seguimiento suave y coordinado hacia el objetivo│
└──────────────────────────────────────────────────────────────┘
                                │
                                ▼
        ┌─────────────────────────────────────────────┐
        │        INTERACCIÓN SOCIAL FINAL             │
        │ ─────────────────────────────────────────── │
        │ • Respuesta hablada o gestual adaptada      │
        │ • Seguimiento visual + coherencia verbal    │
        │ • Empatía con personas con deficiencias     │
        └─────────────────────────────────────────────┘

```


---

### Atenção Visual e Reconhecimento Contextual em Cabeça Pan-Tilt com Modelos Multimodais

O projeto propõe o desenvolvimento de um sistema de percepção e controle baseado em Deep Learning para uma cabeça Pan-Tilt. Utilizando Vision-Language Models (VLMs) e Large Language Models (LLMs), o sistema busca identificar pessoas e interpretar o contexto visual de interação, reconhecendo características como gênero, faixa etária ou presença de dispositivos de mobilidade. A integração entre embeddings visuais e textuais, alinhados via Contrastive Learning, permite criar uma representação semântica unificada. O módulo Speech-to-Text adiciona compreensão verbal, resultando em um sistema que ajusta dinamicamente sua atenção visual e movimento, aplicando Deep Learning multimodal em controle físico e percepção contextual.

---

### V1.0

Desarrollar un sistema de percepción multimodal para robots sociales mediante Vision-Language Models (VLMs) y Large Language Models (LLMs). El objetivo es identificar usuarios y comprender el contexto de interacción a partir de señales visuales y verbales, reconociendo características como edad, género o uso de ayudas de movilidad. El modelo empleará embeddings visuales y textuales alineados con Contrastive Learning y un módulo Speech-to-Text para integrar voz e imagen en un mismo espacio semántico. El desafío es adaptar técnicas de Deep Learning multimodal a entornos reales, permitiendo que el robot ajuste su atención visual y conducta de manera empática e inclusiva.

--- 

### v1.1 Atención Visual y Reconocimiento Contextual en Cabeza Pan-Tilt con Modelos Multimodales

El proyecto propone el desarrollo de un sistema de percepción y control basado en Deep Learning para una cabeza Pan-Tilt. Mediante el uso de Vision-Language Models (VLMs) y Large Language Models (LLMs), el sistema busca identificar personas e interpretar el contexto visual de la interacción, reconociendo características como género, edad o el uso de dispositivos de apoyo. La integración de embeddings visuales y textuales alineados mediante Contrastive Learning permite construir una representación semántica unificada. Con un módulo Speech-to-Text, el sistema amplía la comprensión verbal, ajustando dinámicamente su atención visual y movimiento, aplicando Deep Learning multimodal al control físico y la percepción contextual.

---


🧠 Estrategia: Adaptar VLMs entrenados en ambientes a datasets de personas

1. Entender lo transferible

Aunque los datasets base (como COCO, Ego4D, SayCan, RT-1, RoboVQA) se enfoquen en objetos o entornos:
* Los mecanismos de alineamiento multimodal (imagen↔texto)
* Los encoders visuales (ViT, CLIP, SigLIP)
* Y las pérdidas contrastivas o reconstructivas son completamente reutilizables para tu escenario.

Tu modelo no necesita aprender navegación ni manipulación — solo atención y comprensión visual de personas.

2. Adaptación a datasets humanos

Puedes reutilizar la misma estructura multimodal, pero entrenarla o ajustarla con datasets de interacción social o corporal humana. Algunos datasets útiles:

Tipo de contexto | Dataset sugerido | Aplicación
---|---|---
Rostros y atención | AffectNet, CelebA-HQ, VGGFace2 | Identidad, expresiones
Postura corporal | COCO Keypoints, MPII Human Pose, OpenPose JSONs | Estimar si la persona está parada, sentada, usa muleta
Contexto de discapacidad / movilidad | Human3.6M, EPIC-KITCHENS (subset de manos y apoyo), ATLAS Human Action | Reconocer ayudas físicas, contextos cotidianos
Multimodal visión + texto | AVA Active Speaker + captions, LAION-People subset, VA-RED | Asociar descripciones textuales con imagen o acción
Conversaciones multimodales | SOMA dataset, Social-IQ, MINTS | Aprender correlaciones entre visión y lenguaje

Puedes extraer embeddings visuales de personas y asociarlos con etiquetas textuales simples, por ejemplo:
"persona con bastón", "niño con abrigo", "mujer sentada", "hombre em pé com muleta".

Esto te da un dataset pequeño pero semántico, ideal para fine-tuning ligero o few-shot alignment.

3. Entrenamiento enfocado (sin necesidad de dataset masivo)

Tu meta no es clasificar millones de ejemplos, sino:
* Alinear embeddings de personas reales o simuladas (por ejemplo, capturadas con tu cámara).
* Usar Contrastive Learning o Cosine Similarity Loss para crear una base de correspondencias "imagen ↔ descripción textual".

💡 Ejemplo concreto:
"Embedding de imagen: frame con persona usando muleta"
"Embedding de texto: 'pessoa com mobilidade reduzida'"
Minimizas distancia → el modelo aprende esa asociación.

4. Dataset sintético o aumentado

Si no hay suficientes datos reales de personas con deficiencia o ayudas físicas, puedes:
* Usar Stable Diffusion / SDXL para generar ejemplos controlados ("hombre con muleta", "niña com bengala branca", etc.).
* Aplicar augmentations (blur, rotación, crop) y domain randomization (fondos simples). Esto entrena robustez visual sin depender de grandes colecciones médicas o privadas.

5. Conclusión práctica

👉 Sí puedes aplicar esos modelos, aunque los datasets originales sean de entornos, porque el principio multimodal es el mismo. Solo cambias el dominio del dato: de objetos/ambientes a personas/contextos sociales.

Tu pipeline quedaría así:
```markdown
[Dataset Personas] ─→ [VLM Encoder] ─→ [Embedding Visual]
[Descrições Semânticas] ─→ [Text Encoder] ─→ [Embedding Textual]
                │
                ▼
         Contrastive / Cosine Loss
                │
                ▼
     Modelo Multimodal adaptado a contexto humano
```
---


### V1.2

**Módulo de Visión Social (enfoque reducido y funcional)**
**Proposito Geral**

Dotar al robot de una percepción visual capaz de **iniciar, contextualizar y mantener interacciones sociales básicas**, detectando la presencia humana y las acciones corporales que indiquen intención comunicativa.

La visión actúa como **disparador de la conversación**: cuando detecta una persona (rostro o cuerpo) dentro del campo visual, se activa el sistema de diálogo, integrando la información visual y verbal en un mismo contexto multimodal.

**Entidades visuales reconocidas**

| Entidad | Descripción | Rol funcional |
|----------|-------------|----------------|
| **Rostros / Cabezas** | Segmentación y localización de la cabeza humana. | Detectar presencia humana, activar el inicio de interacción, dirigir la mirada (pan–tilt). |
| **Manos / Brazos** | Máscaras de extremidades superiores. | Reconocer gestos (saludo, señalamiento, intención de comunicación). |
| **Poses corporales** | Estimación estructural del cuerpo (posición y orientación). | Inferir actitud del interlocutor: frente al robot, lateral, distante, etc. |
| **Objetos sobre la segmentación** | Detección de objetos en relación espacial con el cuerpo. | Comprender referencia visual (“persona sostiene un objeto”, “objeto en mesa”), para asociarlo al diálogo. |


**Función principal**
1. Detección social
- **SAM 2-Tiny** segmenta rostros, manos y cuerpos en tiempo real.
- **Presencia** de un rostro humano activa el subsistema de voz (STT/TTS).
- Si no hay rostros detectados por un periodo definido, el sistema entra en modo inactivo.

2. Contextualización multimodal
- Cada entidad visual reconocida se convierte en **contexto visual** del diálogo.
  - Ejemplo: si se detecta que la persona levanta una mano, el LLM interpreta la acción como intención de hablar.

3. Seguimiento e interacción
- El **centroide de cabeza** guía el pan–tilt para mantener contacto visual.
- El **movimiento de manos o brazos** sirve como señal de saludo o llamada de atención.
- Las **poses corporales** ayudan a estimar distancia y orientación, ajustando el tono o el volumen de voz.

4. Integración con el sistema conversacional

```plaintext
[Visión RGB] ─► SAM 2 ─► Máscaras (rostro, manos, pose, objetos)
                        │
                        ▼
             [Contexto visual semántico]
                        │
                        ▼
[ASR / STT] ─► [LLM Conversacional] ─► [TTS / Movimiento]
                        ▲
                        │
                Gatilho visual (“presencia humana”)
```

- El gatillo visual (detección de rostro) inicializa el ciclo conversacional.

- La visión se mantiene activa para actualizar el contexto durante la conversación.

- Las respuestas del LLM pueden incorporar información visual (“veo que estás moviendo la mano”, “parece que estás sosteniendo algo”).

**Métrica de funcionamiento esperada**

```markdown
| Métrica                               | Descripción                                                      | Umbral base               |
|---------------------------------------|------------------------------------------------------------------|---------------------------|
| Latencia de disparo visual → voz      | Tiempo entre detección de rostro y activación del ASR            | ≤ 500 ms                  |
| Tasa de activación falsa              | Conversa iniciada sin presencia real                             | < 5%                      |
| Estabilidad del seguimiento de rostro | % frames con rostro centrado ±ε                                  | > 90%                     |
| Sincronía visión–voz                  | Coherencia temporal entre eventos visuales y respuestas verbales | < 250 ms de desfase       |

```
---
**Extensión futura**
Una vez estabilizada la arquitectura, el mismo flujo puede extenderse con:
- Estimación de emociones faciales (affective vision).
- Detección de atención compartida (shared gaze).
- Contexto visual persistente (memoria a corto plazo de la escena).


**Fluxo de procesamiento visual detallado**
```plaintext
1. Detección / Segmentación global  →  Personas (instancias separadas)
2. Sub-segmentación  →  Partes del cuerpo (cabeza, manos, brazos, torso)
3. Análisis de atributos  →  Dirección de rostro, movimiento, interacción
4. Seguimiento temporal  →  Persistencia de identidades entre frames
```

1. Segmentación global de personas

**Objetivo:** identificar todas las personas presentes como entidades individuales.

- Aquí SAM 2 es ideal: genera máscaras independientes para cada persona, aunque estén parcialmente ocluidas.
- Cada persona recibe un ID persistente en memoria temporal (track_id).
- Esto permite manejar una o más personas sin perder continuidad entre frames.

Ejemplo:
Frame 1 → Persona#1 (izquierda), Persona#2 (derecha).
Frame 2 → misma correspondencia gracias a la memoria de SAM2.

2. Sub-segmentación de partes corporales

**Objetivo:** dentro de cada máscara de persona, identificar las partes relevantes:
- Cabeza / rostro: región superior de la máscara o ROI facial refinada.
- Manos / brazos: subregiones detectadas por pose estimator o modelo de keypoints.
- Torso / postura: eje corporal derivado de los puntos clave (hombros, cadera).

**Cómo hacerlo:**

- Usar la máscara de persona de SAM2 como crop dinámico.
- Dentro de ese crop aplicar pose estimation (p. ej. BlazePose, MediaPipe o OpenPose-light).
- Evitas confusiones entre personas porque cada pose se evalúa dentro de su propia máscara.

3. Análisis de atributos

**Objetivo:** extraer información semántica o cinemática útil.

```markdown
| Atributo             | Fuente                                            | Uso                                                |
|----------------------|---------------------------------------------------|----------------------------------------------------|
| Dirección del rostro | Keypoints faciales (ojos, nariz) o vector de pose | Saber hacia dónde mira la persona (gaze, atención) |
| Movimiento de manos  | Desplazamiento de keypoints o área de máscara     | Detectar gestos de saludo o intención comunicativa |
| Orientación corporal | Vector entre hombros y cadera                     | Inferir si la persona está enfrentando al robot    |
| Relación con objetos | Intersección máscara persona ↔ máscara objeto     | Determinar si la persona sostiene o señala algo    |
```

4. Seguimiento temporal y coherencia

**Objetivo:** mantener continuidad de la información de cada persona a través del tiempo.

- Se mantiene una **memoria temporal** de cada persona (track_id → atributos).
- Los datos se actualizan cuadro a cuadro:
```python
person_memory[track_id].update({
    "head_dir": gaze_vec,
    "hand_motion": delta_pos,
    "pose": skeleton,
    "object_contact": obj_id
})
```

**Así el robot puede:**
- Reconocer quién levantó la mano.
- Cambiar su atención a la nueva persona que apareció.
- Recordar el interlocutor principal de la conversación actual.


---


Aplicación
- Deteccion de personas con caracteristicas especiales
- Reconocimiento de ayudas de movilidad
- Seguimiento visual con Pan-Tilt
        - Estimación de la dirección de la mirada (imagen segmentada)
        - Ajuste de la cámara en función de la atención del usuario


Problemas de modelado  a tiempo real
- costo computacional
- latencia

Experimentos para reconocimiento de voz
- Whisper
- Octabe 2 STT
- ​​Speech-to-Retrieval (S2R): A new approach to voice search

Experiment para segmentacion de imagenes
- SAM 2
- Yolo
https://huggingface.co/docs/transformers/model_doc/sam2

Estructura Semantica de la conversacion
- LLM + Memoria Contextual
- LLM + Knowledge Graph
- LLM + Embeddings Multimodales




- [Experimentos]()
```markdown
═══════════════════════════════════════════════════════════════════════════════
                    RESUMEN EJECUTIVO - COSTO COMPUTACIONAL
                          YOLO v8n-seg | RTX 3050 Laptop 4GB
═══════════════════════════════════════════════════════════════════════════════

┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃   RECURSO      ┃  ANTES   ┃  +5 seg  ┃ +41 seg  ┃  CAMBIO   ┃
┣━━━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━┫
┃ GPU (%)        ┃   10     ┃   29     ┃   24     ┃  +14      ┃
┃ VRAM (MB)      ┃  993     ┃  1325    ┃  1336    ┃  +343     ┃
┃ Temperatura    ┃  55°C    ┃  59°C    ┃  62°C    ┃  +7°C     ┃
┃ CPU (%)        ┃  15.4    ┃  27.0    ┃  37.6    ┃  +22.2    ┃
┃ RAM (GB)       ┃  9.40    ┃  10.71   ┃  10.68   ┃  +1.28    ┃
┗━━━━━━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━┛

═══════════════════════════════════════════════════════════════════════════════
                               CONCLUSIONES CLAVE
═══════════════════════════════════════════════════════════════════════════════

 EFICIENCIA:
   • Modelo ligero: Solo 343 MB de VRAM adicional
   • Temperatura controlada: Incremento moderado (+7°C)
   • Memoria estable: Sin fugas detectadas

 OPORTUNIDADES DE MEJORA:
   • GPU subutilizada: 24-29% (potencial 3x más rápido)
   • CPU elevado: 37.6% sugiere cuello de botella I/O
   • Solución: Aumentar batch size y usar half precision (FP16)

 MÉTRICAS DE RENDIMIENTO:
   • Tiempo carga inicial: ~5-10 segundos
   • Velocidad estimada: ~1 frame/segundo
   • Potencial optimizado: ~3-4 frames/segundo

═══════════════════════════════════════════════════════════════════════════════
Generado: 2025-11-05 | Duración análisis: 41 segundos
═══════════════════════════════════════════════════════════════════════════════
```



---

- [Fuentes para investigar](./Metodología.md)


