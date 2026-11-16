# แหล่งความรู้

รายการนี้จัดตามภาคของหลักสูตร แหล่งเกือบทั้งหมดเป็นภาษาอังกฤษ
ให้ค้นด้วยชื่อที่ระบุไว้ จะเจอหน้าทางการเป็นผลลัพธ์แรก

## คณิตศาสตร์พื้นฐาน (ภาค A)

| แหล่ง | รูปแบบ | ใช้กับบท | จุดเด่น |
|---|---|---|---|
| 3Blue1Brown – *Essence of Calculus* | วิดีโอ YouTube | 01–03 | เห็นภาพว่าอนุพันธ์คืออะไรโดยไม่ต้องท่องสูตร |
| 3Blue1Brown – *Essence of Linear Algebra* | วิดีโอ YouTube | 04 | เห็นภาพเวกเตอร์และเมทริกซ์ในเชิงเรขาคณิต |
| Khan Academy – Calculus 1, Linear Algebra, Statistics & Probability | คอร์สออนไลน์ มีแบบฝึกหัด | 01–05 | ฝึกทำโจทย์ทีละขั้น บางส่วนมีคำบรรยายไทย |
| *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) | หนังสือ อ่านฟรีบนเว็บผู้เขียน | 02–05 | อ้างอิงเชิงลึก ใช้เปิดเมื่ออยากรู้บทพิสูจน์เต็ม |
| StatQuest (Josh Starmer) | วิดีโอ YouTube | 05 | อธิบายความน่าจะเป็นและสถิติแบบช้าและชัด |

## Neural network (ภาค B)

| แหล่ง | รูปแบบ | ใช้กับบท | จุดเด่น |
|---|---|---|---|
| 3Blue1Brown – *Neural Networks* | วิดีโอ YouTube | 03, 06 | ภาพรวม neural network, backpropagation และ transformer |
| Andrej Karpathy – *Neural Networks: Zero to Hero* | วิดีโอ YouTube + โค้ด | 03, 06–13 | แกนหลักของหลักสูตรนี้ ตอนแรกคือ micrograd |
| Michael Nielsen – *Neural Networks and Deep Learning* | หนังสือออนไลน์ฟรี | 03, 06 | อธิบาย backpropagation ละเอียดพร้อมที่มา |

## Language model และ Transformer (ภาค C–D)

| แหล่ง | รูปแบบ | ใช้กับบท | จุดเด่น |
|---|---|---|---|
| Karpathy – *makemore* (ในซีรีส์ Zero to Hero) | วิดีโอ + โค้ด | 08–09 | สร้าง language model ระดับตัวอักษรทีละขั้น |
| Karpathy – *Let's build the GPT Tokenizer* | วิดีโอ + โค้ด (minbpe) | 10 | เขียน BPE เองตั้งแต่ต้น |
| Jay Alammar – *The Illustrated Transformer* | บล็อก | 11–12 | ภาพประกอบ attention ที่เข้าใจง่ายที่สุด |
| Karpathy – *Let's build GPT: from scratch, in code, spelled out* | วิดีโอ + โค้ด | 11–13 | เขียน GPT ทั้งตัวในวิดีโอเดียว |
| Karpathy – nanoGPT และ nanochat | โค้ดบน GitHub | 13 | โค้ดอ้างอิงที่สั้นพอจะอ่านจบ |
| Sebastian Raschka – *Build a Large Language Model (From Scratch)* | หนังสือ + โค้ด (`rasbt/LLMs-from-scratch`) | 09–15 | ละเอียดทีละบรรทัด ครอบคลุมถึง fine-tuning |
| Stanford CS336 – *Language Modeling from Scratch* | คอร์สมหาวิทยาลัย | 10–14 | การบ้านให้เขียนทุกส่วนเอง ระดับลึก |
| Stanford CS224N – *NLP with Deep Learning* | คอร์สมหาวิทยาลัย | 08–13 | พื้นฐานทฤษฎี NLP |

## ใช้งานจริง (ภาค E)

| แหล่ง | รูปแบบ | ใช้กับบท | จุดเด่น |
|---|---|---|---|
| Hugging Face – LLM Course | คอร์สออนไลน์ฟรี | 14–16 | ใช้เครื่องมือมาตรฐานของวงการ |

## เปเปอร์ต้นฉบับ

อ่านหลังเรียนบทที่เกี่ยวข้องแล้วจะเข้าใจง่ายกว่าอ่านก่อน

| เปเปอร์ | ปี | เกี่ยวกับ | ใช้กับบท |
|---|---|---|---|
| Rumelhart, Hinton, Williams – *Learning representations by back-propagating errors* | 1986 | ทำให้ backpropagation เป็นที่รู้จัก | 03 |
| Shannon – *A Mathematical Theory of Communication* | 1948 | ต้นกำเนิด entropy และแนวคิดเดาตัวอักษรถัดไป | 05, 08 |
| Bengio et al. – *A Neural Probabilistic Language Model* | 2003 | language model ที่ใช้ embedding | 09 |
| Bahdanau, Cho, Bengio – *Neural Machine Translation by Jointly Learning to Align and Translate* | 2014 | ต้นกำเนิด attention | 11 |
| Vaswani et al. – *Attention Is All You Need* | 2017 | Transformer | 11–12 |
| Radford et al. – *Improving Language Understanding by Generative Pre-Training* | 2018 | GPT รุ่นแรก | 13 |
