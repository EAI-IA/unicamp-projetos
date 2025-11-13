# Referencias relevantes

**1. Multimodal Fusion and Vision‑Language Models: A Survey for Robot Vision (Han et al., 2025)**
[Aqui](./Bibliografia/Multimodal_Fusion_and_Vision-Language_Models_A_Survey_for_Robot_Vision.pdf)

- Estudia cómo los modelos de visión-lenguaje (VLMs) y técnicas de fusión multimodal se aplican en la visión robótica: segmentación, detección 3D, SLAM, navegación. 
    - Relevancia: provee un buen estado del arte para “captar cómo se usa VLM + visión en robots” lo cual es directamente aplicable a tu proyecto de atención visual / Pan-Tilt.

**2. A Survey on Vision‑Language‑Action Models for Embodied AI (Ma et al., 2024)**
[Aqui](./Bibliografia/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI.pdf)

- Se centra en modelos que integran visión + lenguaje + acción (“Vision-Language-Action” o VLA) en agentes encarnados. 
    - Relevancia: tu módulo de Pan-Tilt + control motor tiene mucho que ver con “acción física condicionada por percepción multimodal”.

**3. ReconVLA: Reconstructive Vision‑Language‑Action Model as Effective Robot Perceiver (Song et al., 2025)**
[Aqui]()

- Propone un modelo VLA con “reconstrucción de atención visual” para mejorar el alineamiento visual-acción.
    - Relevancia: conceptualmente puedes extraer ideas para cómo diseñar la atención (“mirada”) del Pan-Tilt.

**4. A3VLM: Actionable Articulation‑Aware Vision‑Language Model (Huang et al., 2024)**
[Aqui](./Bibliografia/A3VLM_Actionable_Articulation-Aware_Vision_Language_Model.pdf)

- Un VLM centrado en objetos y sus articulaciones, diseñado para robótica. 
    - Relevancia: aunque tu foco es rostro + contexto humano, las ideas de “articulación” y “acción usable” pueden adaptarse al reconocimiento de ayuda de movilidad.

**5. Design of Multi‑Modal Feedback Channel of Human–Robot Cognitive Interface (Zheng et al., 2024)**
[Aqui]()

- Estudia la interfaz multimodal entre humano y robot (visión + otros canales) para reducir carga cognitiva. 
    - Relevancia: tu proyecto también aborda interacción visual + verbal + contextual; este artículo aporta al componente “interacción humano-robot”.

**RoG-SAM: A Language-Driven Framework for Instance-Level Robotic Grasping Detection**
[Aqui](./Bibliografia/RoG-SAM_A_Language-Driven_Framework_for_Instance-Level_Robotic_Grasping_Detection.pdf)

- Estudia la detección y predicción de puntos de agarre (grasping) a nivel de instancia.

- Integra percepción visual con control robótico, permitiendo que el robot ejecute agarres específicos guiados por lenguaje natural.

- Se probó en robots UR5 con cámaras Realsense D435i, logrando 97.5 % de éxito en objetos nuevos y 94.6 % en entornos con desorden.

**Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision**
[Aqui](./Bibliografia/Multimodal_Fusion_and_Vision-Language_Models_A_Survey_for_Robot_Vision.pdf)

- 




| Agente    | Nome                                    | Responsabilidades                                                                                                    | Observações                              |
|-----------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------|
|  Agente 1 | **Agente de Linguagem (LLM Principal)** | - Interpretar o turno do usuário<br>- Decidir quando chamar ferramentas MCP<br>- Gerar respostas ou planos | Atua como **planner cognitivo**                    |
|  Agente 2 | **Agente de Memória**                   | - Gerenciar o JSON persistente<br>- Responder ao MCP (`get_memory`, `update_memory`)<br>- Manter coerência da memória | Pode ser implementado como módulo Python ou micro-serviço |
|  Agente 3 | **Agente Publicador ROS 2**             | - Receber comandos do MCP<br>- Publicar ações simbólicas em ROS 2<br>- Manter logs dos planos                         | Interface entre MCP e o ambiente ROS 2  |



| ID | Persona (perfil) | Diálogo (resumido) |
|----|------------------|--------------------|
| 0  | - Gosto de caçar<br>- Remodelei casas<br>- Meu feriado favorito é Halloween | Usuário: Oi, tudo bem?<br>Agente: Vou treinar perseguição de chitas!<br>Usuário: Você deve ser rápido. Eu adoro caça.<br>Agente: Também gosto de fazer artesanato.<br>Usuário: Legal! Qual sua comida favorita?<br>Agente: Prime rib. E você?<br>Usuário: Frango e macarrão com queijo. |
| 1  | - Tenho 4 irmãs<br>- Acredito em sereias<br>- Amo chá gelado | Usuário: Oi!<br>Agente: Estou com minhas irmãs.<br>Usuário: Vejo Game of Thrones.<br>Agente: Eu também, tomando iced tea.<br>Usuário: O que você faz da vida?<br>Agente: Pesquiso sereias! |
| 2  | - Sou comediante stand-up<br>- Vim de cidade pequena<br>- Bebo Cuba Libre | Usuário: Bom dia!<br>Agente: Isso vira um ótimo texto de stand-up!<br>Usuário: Que séries você fez?<br>Agente: Várias pequenas participações.<br>Usuário: Bebo mojito.<br>Agente: Prefiro Cuba Libre. |


| Resultado Pretendido | Descrição | Como se Observa no Sistema |
|----------------------|-----------|-----------------------------|
| **1. Maior Coerência do Diálogo** | Respostas mais consistentes com o perfil (persona) e histórico. | O agente usa o JSON + MCP antes de responder. |
| **2. Memória Dinâmica Correta** | Lembrar mudanças de estado (ex.: objetos movidos). | Responde corretamente perguntas futuras sobre eventos registrados. |
| **3. Ações Simbólicas Corretas** | Geração de ações planejadas adequadas ao diálogo. | Ação correta publicada no nó ROS 2 (ex.: `remember_object_change`). |
| **4. Redução de Erros de Alucinação** | Menos invenções e contradições. | O agente baseia respostas em memória persistente, não imagina fatos. |
| **5. Melhor Eficiência Cognitiva** | Usa apenas a memória necessária, sem excessos. | Menor número de chamadas MCP desnecessárias (`get_memory`, `update_memory`). |
