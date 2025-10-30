# Funcionalidades del Proyecto

1. Seguimiento Visual Dinámico:
    Detectar y rastrear la posición de una persona en tiempo real usando embeddings visuais derivados de modelos pré-treinados (VLM).

2. Controle Pan-Tilt Inteligente:
    Traducir las coordenadas visuales en movimientos físicos (up, down, left, right) mediante servomotores Dynamixel controlados por U2D2, garantizando transiciones suaves y naturales.

3. Interacción Multimodal (Visión + Voz):
    Capturar el audio del usuario simultáneamente con el seguimiento visual para alimentar un chatbot integrado (Speech-to-Text + LLM).

4. Percepção Contextual:
    Reconocer características básicas del usuario (género, edad aproximada, ayudas físicas o accesorios) para modular la interacción.


## Acciones Realizadas por el Sistema

- Detectar rostro o cuerpo del usuario en el campo de visión.
- Calcular embeddings visuais e inferir dirección de atención.
- Ejecutar movimientos Pan-Tilt (horizontal/vertical) conforme a la posición del usuario.
- Capturar y transcribir voz del usuario en tiempo real (Whisper STT).
- Enviar la transcripción al LLM chatbot para generar respuestas coherentes.
- Mantener sincronía entre atención visual y diálogo, ajustando foco conforme al contexto.



## Tópicos que se Estudiarán

- Vision-Language Models (VLMs): fundamentos, extracción y alineamiento de embeddings visuais.
- Contrastive Learning: técnica para asociar representaciones visuais y textuais.
- Multimodalidade: fusión de señales visuales y auditivas en un mismo espacio semántico.
- Percepção Atencional en Robótica: estrategias de seguimiento visual basadas en aprendizaje profundo.
- Controle Adaptativo Pan-Tilt: mapeo de coordenadas visuales hacia acciones motoras.
- Interação Humano-Robô Simplificada: sincronización entre visión, voz y movimiento.


### Palavras chave
VLM · Embeddings · Contrastive Learning · Pan-Tilt · Multimodalidade · Vision-Language Alignment · Seguimiento Visual · Chatbot · Deep Learning · Atenção Visual




En Robotica es realmente importante las interacciones sociales con cabezas de seguimiento coordinado, para interacciones fluidas.

Setía realmente relevante mantener un punto fijo de seguimiento considerando que la tareas de reconocimiento y seguimiento es un objeto decido a partir de una conversación (ejemplo: alguien pregunta Hola como estas puedes ayudarme <la imagen es procurar una persona> )


Para abordar el problema y probar la 
----

## Descripcion del Proyecto
Objetivo >> Investigar un sistema cognitivo de percepción multimodal en una cabeza robotica Pan Tilt
Para mejorar la calidad de las interacciones sociales entre huamnos y robots.
Motivacion >> lograr que el robot no solo escuche o hable, sino que "mire con intencion", generando una atencion visual coherente con el contenido conversacional.


















# Sistema Cognitivo de Percepción Multimodal en Cabeza Robótica Pan-Tilt

## Descripción del Proyecto — Problema e Hipótesis

El presente proyecto tiene como objetivo investigar un sistema cognitivo de percepción multimodal en una cabeza robótica Pan-Tilt, con el fin de mejorar la calidad de las interacciones sociales entre humanos y robots. En robótica social, las cabezas robotizadas no deben limitarse a captar voz o emitir respuestas, sino que deben ser capaces de mirar con intención, estableciendo un foco atencional que refuerce la comunicación natural. La motivación central es avanzar hacia un sistema de atención visual que esté semánticamente conectado con el contenido conversacional — es decir, que el robot pueda orientar físicamente su "mirada" hacia personas u objetos mencionados durante el diálogo, como hace un humano en contextos sociales.

Este comportamiento se vuelve crítico en aplicaciones donde el robot debe seguir a un interlocutor, establecer contacto visual o buscar a quien está hablando, especialmente cuando hay múltiples personas o referencias espaciales en la escena. A pesar de que existen soluciones de seguimiento visual tradicionales, estas suelen ser desconectadas del lenguaje y no incorporan información semántica de lo que el usuario dice. Por ello, el proyecto propone una arquitectura que integra modelos de lenguaje generativo (LLM), visión computacional y control activo de cabeza, conectando una instrucción lingüística (por ejemplo, "síguela a ella") con un objetivo visual (una persona con ciertas características), y generando movimientos físicos (pan, tilt) que reflejen esa intención de atención.

La hipótesis principal es que esta integración de visión y lenguaje, apoyada en modelos multimodales como CLIP [Radford et al., 2021], SigLIP [Touvron et al., 2023], y LLMs livianos como Phi-2 o Gemma, permitirá generar comportamientos de atención fluida, coherente y socialmente inteligible, superando los métodos de seguimiento visual tradicionales no contextualizados. Trabajos recientes como ReconVLA [Song et al., 2025] y A3VLM [Huang et al., 2024] han demostrado que los modelos visión-lenguaje-acción (VLA) permiten mejorar la percepción activa en robótica, mientras que estudios como [Ma et al., 2024] confirman que la fusión semántica entre visión y lenguaje es clave para lograr comportamientos embebidos más naturales.

## Metodología

La validación de la hipótesis se llevará a cabo mediante el diseño de un sistema multimodal simulador–embebido, compuesto por tres módulos coordinados: percepción visual, lenguaje natural, y control físico de cabeza robótica. Las etapas serán las siguientes:

### 1. Arquitectura Multimodal Vision–Language–Action (VLA)

Se implementará una arquitectura modular que conecte:

* **Vision-Language Model (VLM)**: Se usará CLIP o SigLIP como backbone para generar embeddings visuales y embeddings textuales alineados. Esto permitirá comparar conceptos como "persona con gorro rojo" con imágenes reales en la escena (como en [OpenAI, 2021] y [Touvron et al., 2023]).

* **LLM + STT**: Se usará un modelo de transcripción (Whisper) para convertir voz a texto, y un LLM liviano (como Gemma 2B o Phi-3-mini) para inferir la intención lingüística y extraer la referencia semántica. Esta referencia se convertirá en texto embebido ("persona com muleta", "homem de boné", etc.).

* **Controlador Pan-Tilt**: Se diseñará un generador de comandos discretos (up/down/left/right) que, dados los resultados de similaridad entre texto e imagen (cosine similarity), emita instrucciones para orientar la cabeza robótica hacia el objetivo relevante.

### 2. Simulación y Fusión Multimodal

Todo el sistema será validado inicialmente en un entorno simulado (Unity + ROSBridge o Gazebo), en el que múltiples personas (o avatares) aparecerán con características diversas. La escena simulará casos de referencia ambigua o contextual:

> **Usuario**: "¿Puedes mirar a la persona con bastón?"  
> **Sistema**: (extrae embedding textual, evalúa embeddings visuales de candidatos, gira la cabeza hacia el más similar).

La lógica de control tomará inspiración de estudios como Eagle [Sandha et al., 2023] y VLA-Robot [Han et al., 2025], donde se demuestra que la atención visual guiada por lenguaje puede lograrse mediante alineamiento de embeddings y control discreto activo. Se empleará **Contrastive Learning** como mecanismo de entrenamiento/ajuste del módulo de similaridad si es necesario ampliar el dominio (como propuesto por CLIP y replicado en ReconVLA [Song et al., 2025]).

### 3. Pipeline Experimental

1. **Entrada**: Voz del usuario → Whisper (STT)
2. **Procesamiento**: texto → LLM → extracción de intención ("seguir persona con mochila")
3. **Embedding textual** → VLM
4. **Embeddings visuales** de candidatos en la imagen
5. **Similaridad coseno** (texto–imagen)
6. **Selección del objetivo** más probable
7. **Comando Pan-Tilt** (posición relativa a centro de imagen)

Este pipeline está inspirado en arquitecturas de agentes multimodales como **MM-ReAct** y **ViperGPT** que separan razonamiento semántico y percepción física, conectando ambos mediante embeddings y decisiones de atención. La decisión del foco visual será continua, manteniendo seguimiento si el objetivo se mueve (visión activa).

## Datasets

Para entrenar, adaptar y evaluar los módulos visuales y lingüísticos del sistema Pan-Tilt, se utilizarán únicamente datasets públicos y de libre acceso, que contengan imágenes de personas, descripciones semánticas y/o atributos físicos. El objetivo es construir un entorno multimodal donde sea posible asociar lenguaje natural con contenido visual humano, permitiendo el seguimiento por atención contextual. Los datasets se organizan por tipo de utilidad:

### 1. Detección y Reconocimiento de Personas

| Dataset | Contenido | Aplicación |
|---------|-----------|------------|
| **COCO (Common Objects in Context)** | Imágenes de personas en múltiples contextos y poses, con etiquetas como "person", "backpack", "umbrella". | Detección de personas y preentrenamiento de visión (VLMs). |
| **PETA (PEdesTrian Attribute Dataset)** | 19,000 imágenes con 61 atributos como género, gorro, mochila, silla de ruedas, muletas. | Reconocimiento de atributos físicos para embeddings visuales sociales. |
| **PA-100K** | 100,000 imágenes con 26 atributos de apariencia de peatones (edad, género, ropa, objetos). | Similar a PETA, pero más balanceado y moderno. Ideal para modelos ligeros. |
| **WIDER-Attribute** | Personas en escenas complejas, con 14 atributos: sombrero, gafas, niño/adulto, etc. | Entrenamiento/validación de robustez de embeddings frente a variaciones de contexto. |

Estos datasets permiten crear embeddings visuales discriminativos para personas con características observables, clave para la selección contextual guiada por texto.

### 2. Datasets Multimodales (Imagen ↔ Texto)

| Dataset | Contenido | Aplicación |
|---------|-----------|------------|
| **Flickr30k Entities** | 30 mil imágenes con descripciones detalladas alineadas a regiones específicas. | Evaluación de VLMs (CLIP, SigLIP) en tareas referenciales ("la mujer con sombrero negro"). |
| **RefCOCO / RefCOCO+ / RefCOCOg** | Conjuntos diseñados para referring expression comprehension, donde una descripción como "el hombre con mochila roja" debe localizar una persona en la imagen. | Ideal para tareas de atención visual basada en texto. |
| **Visual Genome** | Millones de pares imagen ↔ pregunta/respuesta, objetos y relaciones visuales anotadas. | Extraer embeddings textuales visualmente coherentes, base para alineamiento VLM. |
| **Open Images (Subset Atribuido)** | Gran colección con atributos como "ocultamiento facial", "muleta", "gafas" etiquetados. | Puede servir para crear ejemplos específicos (ej. "persona con bastón"). |

Estos datasets permiten entrenar o evaluar la capacidad del sistema de entender y ejecutar instrucciones visuales guiadas por lenguaje natural.

### 3. Datasets de Seguimiento Visual para Evaluación

| Dataset | Contenido | Aplicación |
|---------|-----------|------------|
| **LaSOT** | 1,400 videos largos (~2500 frames por objeto), incluyendo personas, con anotación por frame. | Evaluar estabilidad de seguimiento, detección del target en movimiento. |
| **UAV123** | 123 videos aéreos con personas y objetos móviles. | Testear robustez de embeddings bajo ángulos, distancias y fondos variables. |
| **RefVOS (Referential Video Object Segmentation)** | Videos donde se da una instrucción ("la persona con camiseta azul") y se segmenta el objetivo. | Simula tareas reales de atención visual guiada por lenguaje en tiempo. |

Estos datasets se utilizarán para evaluar cuán bien el sistema sigue y mantiene el foco visual en objetivos definidos semánticamente, con cambios de pose o movimiento.

### 4. Datos Sintéticos y Simulación

Se complementará con:

* Generación sintética de escenas en Unity o Blender con avatares humanos variados (edad, vestimenta, posturas).
* Descripciones generadas automáticamente ("niña con sombrero azul") para alineamiento controlado de embeddings en escenarios realistas.

## Métricas de Evaluación

Para validar la eficacia del sistema propuesto, se utilizarán métricas en dos niveles complementarios:

### 1. Evaluación Semántica Multimodal (Lenguaje ↔ Visión)

Evalúa qué tan bien el sistema identifica el objetivo visual (persona u objeto) a partir de una descripción textual.

| Métrica | Descripción | Fórmula / Detalle |
|---------|-------------|-------------------|
| **Cosine Similarity** | Mide la alineación entre el embedding textual y el embedding visual de cada candidato en la imagen. | $\cos(\theta) = \frac{\vec{v}_t \cdot \vec{v}_i}{\|\vec{v}_t\| \cdot \|\vec{v}_i\|}$ <br> Donde $\vec{v}_t$ es el embedding del texto, y $\vec{v}_i$ el de la imagen. |

### 2. Evaluación del Seguimiento Visual (Tracking Atencional)

Mide la capacidad del sistema de mantener la atención visual en el objetivo una vez identificado.

| Métrica | Descripción | Detalle |
|---------|-------------|---------|
| **Success Rate (Tracking)** | Porcentaje de frames en los que el objetivo permanece centrado dentro de un umbral de tolerancia. | Éxito si el objeto está dentro del 10% central de la imagen. |
| **Precision (Tracking Offset)** | Error medio en píxeles entre el centro del objetivo y el centro de la imagen. | $\text{Offset} = \frac{1}{N} \sum_{i=1}^{N} \|C_i^{obj} - C_i^{frame}\|$ |

### 3. Evaluación del Control Físico (Pan-Tilt)

Evalúa la calidad y fluidez de los movimientos de cabeza del robot, aunque sea en simulación.

| Métrica | Descripción | Uso |
|---------|-------------|-----|
| **Angular Error (deg)** | Diferencia angular entre el centro del objetivo y la dirección actual del Pan-Tilt. | Se mide en grados para cada eje (yaw, pitch). |
| **Reaction Latency** | Tiempo desde que se identifica el objetivo hasta que el Pan-Tilt inicia el movimiento. | Mide capacidad de respuesta. |

## Resultados Esperados (Primera Entrega)

En esta etapa inicial, se espera demostrar que el sistema puede ejecutar un ciclo completo de atención visual socialmente coherente, utilizando descripciones lingüísticas simples como entrada, en un entorno simulado. Los siguientes resultados son esperados:

### 1. Comprensión Referencial Eficiente

* **Cosine Similarity > 0.75** promedio entre embeddings texto-imagen del objetivo correcto, validando la alineación semántica entre lenguaje y visión.

### 2. Seguimiento Visual Estable

* **Success Rate ≥ 85%** en mantener el objetivo centrado durante secuencias cortas (3–6 segundos).
* **Precision tracking error < 30 px**, medido entre el centro del objetivo y el centro de la imagen.

### 3. Control Pan-Tilt Natural

* **Angular Error promedio < 7°**, confirmando que la cabeza robótica simula correctamente el direccionamiento visual hacia el objetivo.
* **Latencia de reacción < 1 segundo**, desde la detección semántica hasta el inicio del movimiento Pan-Tilt.

### Validación de la Hipótesis

Estos resultados indicarían que el sistema es capaz de:

* Comprender instrucciones naturales simples relacionadas con personas u objetos visibles.
* Identificar al objetivo correcto mediante embeddings.
* Realizar movimientos físicos (o simulados) socialmente coherentes y precisos.

Esto valida parcialmente la hipótesis de que modelos VLM y LLM coordinados pueden generar atención social multimodal en robots.

## Referencias

Learning Transferable Visual Models From Natural Language Supervision
Alec Radford, Jong Wook Kim, Chris Hallacy et al.
OpenAI – 2021
https://arxiv.org/abs/2103.00020

SigLIP: Scaling and Improving Vision-Language Models with Image Prefixes
Hugo Touvron, Francisco Massa, Nicolas Carion et al.
Meta AI – 2023
https://arxiv.org/abs/2303.15343

A3VLM: Adaptive Agent for Vision-Language-Action Navigation via Multimodal Reasoning
Xin Huang, Tao Wang, Qi Wu, and Xin Eric Wang
ECCV – 2024
https://arxiv.org/abs/2403.05728

ReconVLA: Reference-aware and Context-enhanced Vision-Language-Action Reasoning
Yufei Song, Jiani Liang, Zhiwu Lu et al.
NeurIPS – 2025 (Preprint)
https://arxiv.org/abs/2401.03795

EAGLE: Vision-Language Navigation with Object-level Grounding and Edge-enhanced Graph Reasoning
Rohan Sandha, Xin Eric Wang, William Yang Wang
IEEE Transactions on Pattern Analysis and Machine Intelligence – 2023
https://arxiv.org/abs/2301.08695

Visual Grounding in RefCOCO/RefCOCO+: A Review of Referring Expression Datasets and Models
Licheng Yu, Hao Tan, Mohit Bansal, Tamara L. Berg
ACL Survey – 2022
https://aclanthology.org/P22-3007/

Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations
Ranjay Krishna, Yuke Zhu, Oliver Groth et al.
IJCV – 2017 (aún relevante por su dataset multimodal)
https://arxiv.org/abs/1602.07332

Phi-2: Language Modeling with a 2.7B Parameter LLM
Microsoft Research
Technical Report – 2023
https://www.microsoft.com/en-us/research/blog/phi-2/

