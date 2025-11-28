# Additive manufacturing of Invar 36 alloy  

Guoliang Huang a,b,c, Gongming $\mathrm{He^{a,b,c}}$ , Xiufang Gong d,e, Yong He f, Ying Liu a,b,c,\*, Ke Huang a,b,c,\*\*  

a School of Materials Science & Engineering, Sichuan University, Chengdu 610065, China b Key Laboratory of Advanced Special Materials & Technology, Ministry of Education, Chengdu 610065, China c Sichuan University - Jingwei Huacheng Additive Manufacturing Joint Laboratory, Chengdu 610065, China d Science and Technology on Reactor Fuel and Materials Laboratory, Nuclear Power Institute of China, Chengdu, 610213, China e State Key Laboratory of Long-life High Temperature Materials, 666 Jinshajing West Road, Deyang 618000, China f Dongfang Electric Corporation Dongfang Turbine Co, Ltd, 666 Jinshajing West Road, Deyang 618000, China  

# A R T I C L E  I N F O  

Handling editor. L Murr  

Keywords:   
Invar 36 alloy   
Additive manufacturing   
Microstructure   
Mechanical properties   
Low expansion   
Composite  

# A B S T R A C T  

Invar 36 alloy, renowned for its ultra-low coefficient of thermal expansion (CTE), is a functional Fe–Ni alloy that finds wide applications in aerospace and precision instruments. Additive manufacturing (AM), as a rapid digital manufacturing process, can efficiently and flexibly fabricate Invar 36 alloy parts with complex geometric and exceptional properties. Considering the advantages of AM and the increasing interest and demand for Invar 36 alloy parts fabrication by AM in recent years, it is imperative to provide a comprehensive summary of the current research status and technological advancements pertaining to AM Invar 36 alloy. Firstly, an overview of the AM processes currently employed for fabricating Invar 36 alloy is provided, including laser powder bed fusion, se­ lective laser sintering, directed energy deposition, cold spray additive manufacturing, wire arc additive manufacturing, and binder jetting. Additionally, the microstructure, mechanical properties, and CTE of Invar 36 alloy manufactured by AM are summarized. Even eliminating the post heat treatment, the as-printed Invar 36 alloy can achieve excellent low CTE and mechanical properties, comparable to or exceeding traditional manufacturing processes. Moreover, the advantages and research progress of AM Invar 36 alloy composites are introduced. Enhancing mechanical properties while reducing CTE is a common challenge for both AM Invar 36 alloy and Invar composites. Finally, the technical gaps, research trends, and potential applications of AM Invar 36 alloy are summarized and prospected.  

# 1. Introduction  

Invar 36 alloy is a typical low-expansion alloy discovered by French physicist Charles E´douard Guillaume who won the Nobel Prize in Physics in 1920 for this alloy [1]. In the study of the coefficient of thermal expansion (CTE) of FeNi-based alloys, Guillaume found that the CTE of Fe–Ni alloy was lowest (near zero) when the Ni content was $36\%$ as shown in Fig. 1, so this " invariable steel " was named Invar alloy or Invar 36 alloy [2]. Below the Curie temperature $\mathrm{(T_{C})}$ , the CTE of the Invar 36 alloy is particularly low, with a value of $1.2\times10^{-6}/{}^{\circ}C$ [3]. The physical mechanism underlying this phenomenon can be attributed to spontaneous bulk magnetostriction, whereby the emergence of ferro­ magnetism below the $\mathrm{{T_{C}}}$ results in a contraction of the lattice that partially offsets its thermal expansion with increasing temperature [4]. Beyond the $\mathrm{T_{C},}$ the ferromagnetism changes to a fully paramagnetic behavior, which leads to normal thermal expansion [5]. Invar 36 alloy remains the most widely utilized low-expansion material since its dis­ covery until the present day. With its low CTE and exceptional me­ chanical properties, Invar 36 alloy finds wide applications that demand three-dimensional stability during temperature variation, such as aerospace [6], precision instrumentation [7], oil transportation [8], metrology equipment [9], optics [10], electronic components [11], satellites [12], shadow mask of display tube [13], nuclear field [14] and so on. Some typical applications are illustrated in Fig. 2.  

![](images/9424305dbaa0fb76efb93592311b9a46b352e1c0174b59ec508dcfc176a1e46b.jpg)  
Fig. 1. Impact of varying Ni content on the mean CTE of Fe–Ni alloy [6].  

![](images/6883a742c62b1dc87503e9a08ed0504343159dfbfa4f1041b01406eca8812677.jpg)  
Fig. 2. Typical applications of Invar 36 alloy.  

Currently, the traditional manufacturing processes for preparing Invar-parts mainly include casting [15], forging [16], powder metal­ lurgy [17,18], welding [19], and rolling [20]. Despite the advantages of these processes, there are still some limitations. Firstly, traditional manufacturing processes have limited freedom and efficiency in pre­ paring parts [21]. Secondly, machining process generates highly ductile chips that accumulate on the cutting tool surface, resulting in tool wear and productivity reduction. In addition, work hardening and low ther­ mal conductivity of Invar alloy also reduce cutting tool life [22]. Thirdly, the application of Invar parts with complex geometries and lightweight structures in Fig. 2 presents a unique challenge, as these components are difficult to prepare using traditional forming processes. Therefore, it is extremely important to find a new manufacturing process for Invar 36 alloy.  

Additive manufacturing, also known as 3D printing, is a digital fabrication technology that rapidly constructs objects in a layer-by-layer approach [23]. Over the past two decades, additive manufacturing has been considered a revolutionary manufacturing technology due to its superiority over traditional subtractive processes [24], and is becoming one of the most disruptive technologies in Industry 4.0 [25]. This is due to its multiple advantages: (i) near-net shape manufacturing produces parts that are suitable for their final applications or require minimal post-processing [26], (ii) AM can fabricate complex geometric compo­ nents, which cannot be machined by traditional methods [27], (iii) rapid manufacturing, short production lead time and fast delivery [28], (iv) high utilization rate and environmental friendliness [29], (v) the inte­ grated design of “material - structure - performance - function compo­ nent” [30]. As a result, there is considerable excitement about AM around the world, and significant investments have been (or are being) made for research and capacity building according to Wohlers Report 2023. Therefore, the AM-fabricated Invar 36 alloy holds significant implications and merits attention in study. Additive manufacturing has been proved suitable for Invar 36 alloy, and the development of additive manufacturing Invar 36 alloy holds significant promise [31]. The application of additive manufacturing in various alloy systems, including titanium alloys [32], superalloys [33], steels [24], high-entropy alloys [34], aluminum alloys [35], magnesium alloys [36], and copper alloys [37], has been widely investigated and comprehen­ sively reviewed in the literature. These reviews effectively promote rapid access to a more comprehensive and up-to-date knowledge of AM alloy for researchers and engineers. However, there is a lack of reviews focusing on Invar 36 alloy, since AM Invar 36 alloy research has just started. Therefore, a recapitulative review of the additive manufacturing for Invar 36 alloy is essential to inform scholars and engineers about the progress of the Invar 36 alloy prepared by additive manufacturing.  

The objective of this paper is to provide a comprehensive summary of the additive manufacturing currently available for Invar 36 alloy, including their corresponding microstructures, mechanical properties, and thermal properties. Furthermore, this study investigates the char­ acteristics of Invar alloy matrix composites prepared by additive manufacturing techniques. Finally, this paper presents an analysis of the current problems and provides insights into the future development direction of additive manufacturing for Invar 36 alloy.  

# 2. overview of AM-fabricated Invar 36 alloy  

# 2.1. Classification of AM processes for Invar 36 alloy  

The ISO/ASTM 52900:2015 standard defines AM processes into the following seven categories: powder bed fusion, directed energy depo­ sition, sheet lamination, photo-polymerization, material jetting, mate­ rial extrusion, and binder jetting [38]. Alternatively, the AM process can be further subdivided according to feeding state (powder, wire, or sheet), energy source (electron beam, laser, or electric arc), and feeding method (blowing or feeding powder or powder bed) [39]. Although there are many additive manufacturing processes, fewer processes are used to prepare Invar 36 alloy compared to other alloys [40]. Currently, the additive manufacturing techniques utilized for Invar 36 alloy comprise selective laser sintering (SLS), laser powder bed fusion (LPBF), directed energy deposition (based on laser heat source, DED), cold spray additive manufacturing (CSAM), binder jetting (BJT) and wire arc ad­ ditive manufacturing (WAAM). The schematic diagram of various ad­ ditive manufacturing processes is illustrated in Fig. 3.  

Laser powder bed fusion (LPBF), also known as selective laser melting (SLM), is a prototypical metallic additive manufacturing pro­ cess. As illustrated in Fig. 3(a), the LPBF process employs a high-energy laser beam as the energy source and follows a predetermined laser path to scan each layer of the powder bed, resulting in localized fusion and solidification of the metal powder, ultimately leading to the formation of a three-dimensional component [41]. The LPBF technology is consid­ ered to be one of the most productive and promising technologies, so LPBF is the most widely additive manufacturing process used to prepare Invar 36 alloy [21,42,43]. The technology is developed from selective laser sintering (SLS, shown in Fig. 3(b)), and the two forming principles are similar [44]. SLS does not require support and is often used for forming non-metallic components, such as ceramic, resin, and metal powder binder mixtures [45]. Currently, the research on the production of Invar 36 alloy using SLS technology is not comprehensive, and only the impact of SLS process parameters on the quality of molding has been investigated [46].  

![](images/a14813daa7fd615b0c5a247a2d0756bc45938591ce4b0ebbcdddbd42b441d7bd.jpg)  
Fig. 3. Schematic diagram of the current additive manufacturing of Invar 36 alloy: (a) laser powder bed fusion (LPBF), (b)selective laser sintering (SLS), (c) directed energy deposition (DED), (d) wire arc additive manufacturing (WAAM), (e) cold spray additive manufacturing (CSAM), (f) binder jetting (BJT).  

Besides the LPBF technology, another well-known metal additive manufacturing process is the DED technology [47]. As illustrated in Fig. 3(c), DED technology refers to additive manufacturing that uses a high-powered laser beam to allow the laser to create a molten pool in the deposition area and move at high speed, with the material being fed directly into the high-temperature molten area in powder or filament form, melted and deposited layer by layer to ultimately form the component [48]. Compared with LPBF technology, DED technology has the advantages of low cost, large forming build, high production rate, multi-material forming, and component repair capability [49]. Because Invar 36 alloy is often used to prepare large dies and the prepared dies sometimes need to be repaired, DED technology takes full advantage of manufacturing Invar 36 alloy [50]. Additionally, the DED technology is commonly employed for the preparation of Invar alloy composites, such as Ti–6Al–4V/Invar [51] and MnCu/Invar [52] gradient composites. Furthermore, the WAAM technology forming process is also a material deposition process [53]. As shown in Fig. 3(d), the wire arc additive manufacturing (WAAM) technology utilizes electric arcs generated by welding machines, such as tungsten inert gas (TIG) (also called gas tungsten arc welding, GTAW), molten inert gas (MIG) (also called as gas metal arc welding, GMAW), and plasma arc welding power (PAW), as a heat source [54]. By adding metal wire, layers are deposited on the substrate following a predetermined path under program control until the metal part is nearly net-formed [55]. The WAAM technology is considered one of the most cost-effective methods for fabricating large metal parts. The Invar 36 alloy aerospace tooling, manufactured by WAAM, exhibits exceptional performance and has been successfully implemented [56].  

All the above additive manufacturing requires a heat source to form, however, there are also additive manufacturing that do not require a heat source to form, namely cold spray additive manufacturing (CSAM) and binder jetting (BJ). Fig. 3(e) shows a schematic of CSAM, which can be seen that CSAM uses a gas nozzle to accelerate metal powder to su­ personic velocity and spray it onto the surface of a substrate to produce a uniform metal coating. Through iterative execution of this process, a three-dimensional object is gradually constructed by means of stacking [57]. CSAM is characterized by a wide range of materials for application, extremely high powder deposition efficiency and deposition rate, su­ perior material properties after processing, unrestricted size of pro­ cessed workpieces, and environmental friendliness [58]. Unlike laser additive manufacturing or conventional thermal spray technologies, the unique cold properties of CSAM technology effectively avoid oxidation, acute phase transition, grain growth, and cracking that may result from thermal stress [59]. Therefore, it is particularly suitable for preparing  

G. Huang et al.  

![](images/45f183b69dec0ddb7a50fd1c733ecd21d3ada9fa56c0e43867674c62e8b9ccd8.jpg)  
Fig. 4. (a) Number of published papers on AM-fabricated Invar 36 alloy; (b) percentage of the number of papers of different types of AM technology. Data wer obtained from papers published before November 2023 in the Web of science.  

Table 1 Main research of additive manufacturing for Invar 36 alloy.   


<html><body><table><tr><td>AM</td><td>Formability</td><td>Post-treatment</td><td>Properties</td></tr><tr><td>LPBF[21] [72, 73],</td><td>Parameter optimization, defects</td><td>Hot isostatic pressing, heat treatment</td><td>Thermal expansion, tensile properties, fatigue, hardness</td></tr><tr><td>SLS[46]</td><td>Parameter optimization, density, surface roughness</td><td>/</td><td>/</td></tr><tr><td>DED[69, 70]</td><td>Defects</td><td>Heat treatment</td><td>Thermal expansion, tensile properties</td></tr><tr><td>WAAM [71]</td><td>/</td><td>Heat treatment</td><td>Thermal expansion, tensile properties,</td></tr><tr><td>BJT[64]</td><td>Defects,surface roughness</td><td>Electropolishing</td><td>hardness /</td></tr><tr><td>CSAM [59]</td><td>Parameter optimization, density, defects</td><td>Heat treatment</td><td>Thermal expansion, tensile properties</td></tr></table></body></html>  

large Invar 36 alloy dies or modifying part [60].  

As illustrated in Fig. 3(f), the BJT technology operates by dispensing the binder onto the powder along a predetermined path through the printer nozzle [61]. The powder materials receiving the binder are bonded to each other and solidified, and the rest of the powder remains loose. This step is repeated layer by layer until the preliminary parts are made, and then the loose powder is removed and sintered and solidified. The adhesive is removed to fuse the powder particles, and finally the parts with the required density and strength are obtained [62]. The BJT technology demonstrates notable advantages in terms of its exceptional precision in formation, cost-effectiveness, and efficiency [63]. With the advantages mentioned above, BJT technology has manufactured Invar 36 alloy devices used in the field of optics [64].  

# 2.2. Current research status of AM-fabricated Invar 36 alloy  

Six additive manufacturing technologies for Invar 36 alloy are described above, and each of them has its characteristics. However, it is worth noting that the current state of Invar 36 alloy used for additive manufacturing is not yet fully developed. The published relevant papers on AM-fabricated Invar 36 alloy were searched in the Web of Science database on November 20, 2023, as shown in Fig. 4. The DED technol­ ogy was initially employed for the fabrication of Invar 36 alloy, while the advantages of additive manufacturing were first recognized in 2002 (Fig. 4(a) is based on Web of science database). The current ranking of the most widely adopted AM technologies for Invar 36 alloy was as follows: LPBF, DED, and WAAM technology (in Fig. 4(b)). It is worth noting that AM-fabricated Invar 36 alloy currently has only 59 papers, even including conference papers and presentations. Hence, further research and development is still ongoing.  

The main research conducted on AM-fabricated Invar 36 alloy, as illustrated in Table 1, offers a clear recognition of the current state of research. The LPBF process has been widely studied as the primary method for investigating Invar 36 alloy. Most research focuses on examining how the LPBF process parameters affect formability, me­ chanical properties (mainly tensile [65] and fatigue [66] properties) [67], and thermal expansion [68]. However, there is a relatively limited investigation into post-treatment methods due to their minimal impact on both microstructural features and properties [21]. The SLS technol­ ogy is of lower quality compared to the LPBF technology, and only the impact of process parameters on Invar 36 alloy formability has been investigated [46]. The DED technology focuses on microstructure evo­ lution [50], tensile and [69] thermal expansion properties [70]. WAAM technology is second only to LPBF technology, mainly focusing on the tensile properties and thermal expansion of Invar36 alloy manufactured by WAAM [71]. The influence of process parameters and post-treatment on the formability of Invar36 alloy fabricated by the BJT process was investigated [64]. The research content of Invar 36 alloy manufactured by CSAM technology is like that of DED technology. The reality is that application scenarios require specific AM processes for effective adaptation.  

Currently, despite the numerous benefits of additively manufactured Invar 36 alloy, there is a lack of systematic understanding regarding understanding regarding its research status, including microstructure characteristics, mechanical properties, thermal properties, and knowl­ edge gaps. Therefore, to fully leverage the advantages of additive manufacturing, a comprehensive overview is provided for the Invar 36 alloy produced by additive manufacturing, aiming to enhance the practical application of the AM process.  

# 3. Microstructure  

# 3.1. Formation Defects  

In additive manufacturing processes, achieving high relative density $(>99.5\%)$ of manufactured parts is often the dominating objective for optimizing and controlling process parameters [34]. If not, the high porosity in the component is prone to crack extension and significant degradation of mechanical properties [67]. Therefore, subsequent studies mechanical properties, and thermal expansion can only be per­ formed if it is ensured that the material is dense $(\mathrm{RD}\geq99\%)$ [74]. The kinds of defects observed in AM-fabricated parts include cracks, spher­ oidization, unfused powder, pores, delamination, warping, and keyhole porosity [75]. Invar 36 alloy is a face-centered cubic metal with excel­ lent weldability [31], so there are almost no weaknesses such as forming difficulty, brittleness, and thermal cracking during additive  

![](images/f3bd528d546d7b34bb63a3f2dabf9e1c03da4a3e172ff350e80423c1f6a1eabf.jpg)  
Fig. 5. Formation Defects of AM-fabricated Invar 36 alloy. (LPBF [21], SLS [46], CSAM [59], and BJT [64]). Detailed CSAM conditions: N1-AS is Nitrogen/3.0 $\mathbf{MPa}/800^{\circ}C/\mathbf{i}$ mpact velocity of $752.1\ \mathrm{m}/s\ \$ , N2-AS is Nitrogen/ $\mathrm{'5.0\MPa/800\^{\circ}C/i}$ mpact velocity of $807.6~\mathrm{m}/s$ , and He-AS is Helium ${\mathrm{\prime3.0~MPa}}/{800}^{\circ}C/{}$ impact velocity of $1097.4~\mathrm{m}/s$ .  

![](images/b6f535b6591e40c12fa0a9f38a851844275e5dae9aaa7430c0a5058bef28eac9.jpg)  
Fig. 6. Relative density of the AM-fabricated Invar 36 alloy.  

manufacturing [65].  

Fig. 5 shows common defects inside the AM-fabricated Invar 36 alloy, and it can be found that the defects are almost dominated by holes. For the preparation of Invar 36 alloy by LPBF technology, insufficient laser energy density may lead to incomplete fusion of the raw powder, leading to either inadequate bonding or unfused powder within the material. Excessive laser energy density can elevate the surface temperature beyond the evaporation threshold of the alloy, causing to recoil of molten material and particles from the heat-affected zone, leading to the ejection of powder and melting that creates large irregular voids. In addition, inert protective gases may be trapped in the voids, forming spherical pores [76]. Similarly, the defects produced by SLS forming of Invar 36 alloy are also related to the laser energy density [46].  

Formation defects in CSAM-prepared Invar 36 alloy are related to the propellant gas. Chen et al. [59] compared the effects of two propellant gases, helium, and nitrogen, on the densities of specimens. It was observed that the utilization of nitrogen as a propellant gas resulted in higher impact velocity, which effectively mitigated porosity defects at elevated pressures. This is owing to the gradual increase in impact ve­ locity with the increase in gas pressure and temperature, as well as the severe specimen. When helium is employed as the propellant gas, the impact velocity can reach $1097.4~\mathrm{m}/s$ , significantly higher than that of nitrogen-treated specimens, resulting in higher densities. The densities of Invar 36 alloy manufactured by the BJT technology are related to the printing parameters and the sintering process, where often internal de­ fects are present after sintering, giving the advantage of using hot isostatic pressure to enhance the density of Invar 36 alloy. The surface roughness of Invar 36 alloy can be further reduced through sandblasting and electrochemical polishing, simultaneously enhancing its quality [63]. Despite the defects within the AM-fabricated Invar 36 alloy, the heat input may be adjusted by optimizing the process parameters, which in turn improves the densification of Invar 36 alloy [65].  

Fig. 6 demonstrates the relative densities of Invar 36 alloy prepared by LPBF, CSAM, and BJT technologies at the most excellent process parameters reported in the literature. The relative density of Invar 36 alloy manufactured by LPBF technology can exceed $99.5\%$ after asLPBFed condition or post-treatment (heat treatment $^+$ hot isostatic pressing), while the CSAM technology prepares a density of up to $99.98\%$ , and the BJT technology prepares an alloy up to $99.88\%$ after HIP. Currently, the maximum relative density of as-LPBFed Invar 36 alloy reported in the reference is $99.99\%$ by $\mathbf{x}$ -ray computed tomogra­ phy [68].  

![](images/73d700b57d0542cc42a2455de1081355e86272093c1fc6650b57e6733ce74df6.jpg)  
Fig. 7. XRD patterns of the AM-fabricated Invar 36 alloy: (a) as-LPBFed [80],(b)as-WAAMed [81], (c) as-DEDed [52], (d) as-CSAMed [59]  

![](images/c17ce40945662e7fac0a16a15d7be443d138f93df87368e069997bc23710aa81.jpg)  
Fig. 8. Optical microscope images of the microstructure of as-LPBF specimens at different laser power: (a) 250 W, (b) 300 W, (c) $350~\mathrm{W}$ , and (d) 400 W [83].  

In addition to the examination of light microscopy and SEM figures, the utilization of high-speed infrared imaging and $\mathbf{\boldsymbol{X}}$ -ray computed to­ mography (XCT) for observing defect formation during evolution also plays a crucial role in ensuring manufactured quality [77]. Yakout et al. [78] found that defects in as-LPBFed Invar 36 alloy were primarily caused by splashing at laser energy density below $86.8~\mathrm{J/mm}^{3}$ , while higher values resulted in delamination and hot spot formation when combining high-speed infrared thermography and infrared pyrometer. By precisely controlling the ejection speed and direction during on-line monitoring, effective control of Invar 36 alloy formation quality can be achieved. Yang et al. [65] utilized In-situ XCT to investigate the damage evolution resulting from defects under mechanical loading. The results demonstrate that internal defects within the Invar 36 alloy manufactured via LPBF at a scanning speed of $400\ \mathrm{mm/s}$ cause ductile fracture during the tensile process, while a speed of $1000\mathrm{mm}/s$ leads to brittle fracture. Similarly, the optimization of scanning speed can be effectively regulated the defects between the printed layers and achieve superior manufactured quality.  

![](images/d0288b25810048098c3f98473a170279abc46e4163bac491d6b683ee4c69294b.jpg)  
Fig. 9. Microstructure of as-LPBFed Invar 36 alloy: (a) and (c) of optical mi­ crographs in the specimen side surface, (b) and (d) of optical micrographs in the specimen cross-section [80].  

![](images/6f08fab378daa9fcdced3b03acf3907835cd63881601f04ad334f34a9e18b89d.jpg)  
Fig. 10. EBSD diagrams of as-LPBFed Invar 36 alloy: (a) and (b) of the side surface and cross-section Inverse polar figures, respectively, and (c) and (d) of the side surface and cross-section phase diagrams, respectively [80].  

Currently, only the relative density of Invar 36 alloy prepared by LPBF, SLS, and CSAM processes has been reported; other AM processes have not been studied yet. The distribution of defects in the AMfabricated Invar 36 alloy specimen is stochastic, resulting in inade­ quate properties dispersion at different positions within the same Invar 36 alloy specimen or insufficient properties repeatability under identical parameters [66]. Additionally, thermal properties [76] and tensile properties [67] in AM-fabricated Invar 36 alloy are highly sensitive to process-induced defects. It is imperative to investigate the relationship between different process parameters-defects-density to obtain high-property Invar 36 alloy components. The use of numerical simu­ lation in the powder melting and solidification process allows for analyzing micro perspective, while high-speed camera enables real-time monitoring of the manufacturing process, establishing a comprehensive correlation.  

# 3.2. Microstructure as AM-fabricated  

Additive manufacturing is a rapid forming process with a rapid nonequilibrium solidification process, which is different from traditional manufacturing processes (e.g. casting, forging, rolling) [79]. Fig. 7 shows the XRD patterns of the as-LPBFed (a), as-WAAMed (b), as-DEDed (c), and as-CSAMed (d) Invar 36 alloy. The harmful bcc- $\mathbf{\alpha}_{\cdot\propto}$ phase is not detected within the XRD detection limit, suggesting its absence or negligible content. Obviously, the predominant phase observed is pri­ marily composed of the fcc-γ phase (For ease of description, the Austenite, the FCC-austenitic, γ[Fe, Ni] and $\boldsymbol{\upgamma}$ -(Fe–Ni)) is denoted as fcc-γ.). It also highlights the advantages of additive manufacturing, as a higher number of fcc- $\boldsymbol{\gamma}$ phases enhance plasticity of Invar 36 alloy.  

# 3.2.1. Microstructure of LPBF-fabricated Invar 36 alloy  

Laser powder bed fusion is the current most widespread used addi­ tive manufacturing for manufacturing Invar 36 alloy, so the analysis of the microstructure characteristics of the LPBF technology is reported below firstly. Whether AM-fabricated Invar 36 alloy or other metals, the optimization of process parameters plays an important role [82]. The optimization of parameters not only determines the forming quality but also directly affects the microstructure and performance. Fig. 8 shows the change of microstructure in as-LPBFed Invar 36 alloy under different laser powers (other process parameters are fixed.) [83]. The micro­ structure consists of many molten pools (fish scale-shaped track) and columnar grains penetrating it at all laser powers. At the laser power of $250\mathrm{W}$ , the molten pool boundary (MPBs) exhibits a semicircular shape in Fig. 8(a). As the laser power is increased to 300 W, 350 W, and $400{\mathrm{W}}_{\cdot}$ , the shape transforms into a goblet-like shape in Fig. 8(b–d). In addition, Asgari et al. [83] found that the more chaotic the MPBs with a goblet-like shape, the better the density in Fig. 8(d). The higher the laser power, the more fully the metal melts in the lap zone (overlap area of molten pool), resulting in a better metallurgical bond when the scanning spacing, scanning speed, and powder layer thickness are fixed [84].  

Further analysis of the detailed microstructure of the Invar 36 alloy is needed. Fig. 9 demonstrates the microstructure of the as-LPBFed spec­ imen [80]. As shown in Fig. 9(a) and (c), it is evident that the side of the specimen exhibits a semicircular “fish scale” melt pool, with columnar grains passing through it. The white traces of the melt pool are discernible in the cross-section, as shown in Fig. 9(b) and (d). In contrast to the sides, the grain boundaries appear irregularly polygonal, which precisely matches the cross-sectional morphology of columnar γ grains. The discrepancy between the grain boundaries observed in the side and cross sections suggests that the γ columnar grains witnessed during LPBF technology exhibit growth along the direction of the maximum tem­ perature gradient, as shown in Fig. 9(b).  

EBSD diagrams are presented in Fig. 10 for a better insight into the microstructure. In Fig. 10(a) and (b), distinct colors correspond to different grain orientations. The different colors of both transverse and longitudinal grains indicate no clear preference in grain orientation. This may be due to the scanning strategy of rotating the adjacent layers by $67^{\circ}$ , which changes heat flow direction and inhibits texture formation [85]. By adjusting the scanning strategy, as-LPBFed Invar 36 alloy can obtain the common ${<}001>$ texture of face-centered cubic metals [73]. In addition, Fig. 10(b) can also clearly see the lots of small columnar grains inside the laser-scanned channel. Fig. 10(a) also illustrates the prevalence of columnar grains that penetrate several microns on the side, which is consistent with the observations in Figs. 8(a) and Fig. 9 (a–c), demonstrating epitaxial growth of columnar grains.  

The phase identification by XRD has limitations; therefore, further observation of the phase was conducted based on Fig. 10(c) and (d). The blue region represents the fcc- $\cdot\gamma$ phase, accounting for approximately $95\%$ of the total area, while the green region corresponds to the bcc- $\mathbf{\alpha}\cdot\mathbf{\alpha}\propto$ phase, constituting only about $0.5\%$ of the total area. The Invar 36 alloy manufactured by LPBF technology has almost no partial precipitation because Invar 36 alloy belongs to a face-centered cubic lattice and so­ lidifies faster during the manufacturing process so that bcc $\upalpha$ does not precipitate out from the fcc-γ phase in time [21].  

![](images/dfef462c60aa4ececbd1b86ce9d8d012c4e068ac7f399d4b1bcfaba3f9f10a74.jpg)  
Fig. 11. SEM images of as-CSAMed specimen Invar 36 alloy: (a) $3\mathrm{MPa}$ pressure nitrogen sprayed condition with the velocity of $752.1~\mathrm{mm}/s$ , (b) 5 MPa nitrogen sprayed condition with the velocity of $807.6~\mathrm{mm}/s,$ (c) 2 MPa helium sprayed condition with the velocity of $1097.4~\mathrm{mm}/s$ [59].  

![](images/a614599d1fdd0b55e2bcf29bf941dc9abba55d9ef548ca9c2fcbdf263ea2fb9b.jpg)  
Fig. 12. As-CSAMed specimen EBSD diagram of Invar 36 alloy: (a–b) $\mathbf{N}_{2}$ -sprayed, (c–d) He-sprayed; (a, c) inverse pole figures (IPF), (b, d) grain boundary maps [59].  

# 3.2.2. Microstructure of as-CSAMed Invar 36 alloy  

Fig. 11 displays the SEM diagram of the Invar 36 alloy manufactured by CSAM technology under nitrogen $\left(\Nu_{2}\right)$ and helium (He) spray. Based on the schematic diagram presented in Fig. 3(e) showcasing the CSAM technology, it is known that the process uses high-pressure gas injection molding, so the type, pressure, and speed of the injection gas have a great influence on the molding quality [86]. As shown in Fig. 11(a–c), vortex and eddy mode microstructures are generated under different injection gases and pressures, and the tissues are also different. Specif­ ically, specimens manufactured by high-pressure nitrogen injection  

G. Huang et al.  

![](images/6863d27f990433451e909c0e4d13aaeafe8d0a9890f6bee08d7fd7ccb95dc4a6.jpg)  
Fig. 13. SEM images of BJT-fabricated Invar 36 alloy after sintering: (a) as-printed surface, (b) sandblasted surface, (c) and (d) of electrochemically polished surface [64].  

![](images/e2b2e20974578bb4906215463e1cc9f82bc4d79946e93520bd424b5d4d11634f.jpg)  
Fig. 14. Formation of surface crack owing to the capillary action of the dried binder [64].  

show more severe plastic deformation than those formed by low-pressure nitrogen injection in Fig. 11(a) and (b). The mechanical interlocking phenomenon occurs due to the serious plastic deformation of high-pressure nitrogen injection-forming specimens. Compared with $\mathbf{N}_{2}$ -sprayed specimens, there are elongated and refined grains on the deformed grain boundary in He-sprayed specimens, while relatively large equiaxed grains exist inside the particles in Fig. 11(c).  

To further reveal the changes in the microstructure, the character­ ization of as-CSAMed Invar 36 alloy can be revealed by EBSD. As illus­ trated in Fig. 12, $\mathrm{N}_{2^{-}}$ and He-sprayed specimens exhibit a representative double-peaked grain size distribution with a non-uniform deformation pattern in the sprayed specimens. Nanoscale ultrafine grains and elon­ gated grains are present in the boundary region between the severely deformed grains. Compared to the $\mathbf{N}_{2}$ -sprayed specimen, the He-sprayed specimen shows a larger area of equiaxed grains in the intergranular region in Fig. 11(c). This phenomenon indicates enhanced dynamic recrystallization and more prominent grain refinement at higher particle impact velocities. EBSD analysis reveals the average grain size of the Hesprayed specimen is $0.443~{\upmu\mathrm{m}}$ , which is lower than that of the $\mathbf{N}_{2}$ - sprayed specimen $(0.561\upmu\mathrm{m})$ , while both He- and $\mathbf{N}_{2}$ -sprayed specimens retain their original equiaxed grains in the deformed state in Fig. 11(a) and (c). The grain boundary diagrams depict HAGBs (high-angle grain boundaries, $>15^{\circ}\bar{.}$ as blue lines and LAGBs (low-angle grain bound­ aries, $\mathit{\Theta}<15^{\circ}.$ ) as red and green lines in Fig. 12 (c) and (d). Hyperfine grains at the grain boundaries are mainly characterized by HGABs [87]. It indicates the formation of highly oriented nanoscale equiaxed grains because of dynamic recrystallization during the CSAM technology. Meanwhile, LAGB can be observed near the ultrafine grains and inside  

G. Huang et al.  

![](images/a55590d8dbd988e98863d68b9d39880c5886129948a72bcb604859c569b35b7e.jpg)  
Fig. 15. Invar 36 alloy manufactured by PAW-based WAAM: (a) aeronautical tooling, (b) microstructure of Zone I, (c) microstructure of Zone II [56]  

![](images/fc2a23bba56eae8fc19bec240d7325adaa0a041cb0edcf8a04d78aff0175bad1.jpg)  
Fig. 16. Microstructure of cross-section (XY) and longitudinal section(XZ) of as-WAAMed Invar 36 alloy via PAW and GMAW processes [54]  

the larger grains, which indicates the presence of high dislocation den sity during the high-speed impact of CSAM deposition.  

# 3.2.3. Microstructure of as-BJTed Invar 36 alloy  

Fig. 13 shows the SEM diagram of the Invar 36 alloy specimens manufactured by BJT technology. Preparing Invar 36 alloy by BJT technology is the use of binder bonded powder and then sintered. Fig. 13 (a) is a typical morphology of the specimen after sintering, where there are many pores and cracks on the surface, which is highly rough, the reason for the formation analysis is shown in Fig. 14. The powder will coalesce upon spraying, but as heat is absorbed, the binder powder surface of the powder will rapidly evaporate, thus altering the balance of capillary pressure and interparticle tension. This phenomenon leads to agglomeration of the powder particles, resulting in numerous cracks and voids on the green body surface.  

To reduce the surface roughness of the as-BJTed specimen, surface treatments such as sandblasting and electrochemical polishing are often performed [88,89]. It can be observed from Fig. 13(b) and (c-d) that the surface roughness of the specimen is significantly reduced after sand­ blasting and electrochemical polishing compared with Fig. 13(a), while the effect of electrochemical polishing is better. It is noteworthy that the relative density of Invar 36 alloy manufactured by BJT technology is comparatively lower than other methods, as shown in Fig. 6. The surface roughness of the specimen manufactured by the SLS technology is also higher, and the lower the roughness of the specimen, the higher the density of the Invar 36 alloy [46].  

# 3.2.4. Microstructure of as-WAAMed Invar 36 alloy  

WAAM technology offers the advantages of simple equipment and lower cost when compared to other additive manufacturing [90]. Common WAAM technology is divided into three types: PAW-based, GMAW-based, and GTAM-based WAAM technology [54]. Aldalur et al. [56] used PAW-based WAAM technology to manufacture the specialized Invar 36 alloy aeronautical tooling, as depicted in Fig. 15(a).  

![](images/fd57aa946e4d04e026c0764e4b58068f68855f87aa2accc940a8b29fe156fc32.jpg)  
Fig. 17. Microstructure of GTAW-based WAAM Invar 36 alloy: (a, c, d) heat input of $200\ \mathrm{J/mm}$ , (b, d, e) heat input of $550~\mathrm{J/mm}$ (a) and (b) optical mi­ croscope images, (c) and (d) of grain boundary maps, and (e) and (f) of KAM diagrams [81].  

![](images/d1d483d7a80fa221f9749a3fae5fe8ec64253c81a2f1d30ea682c1bae2800cb6.jpg)  
Fig. 18. Macrostructure of the as-DEDed Invar 36 alloy specimen [69].  

Fig. 15(b) and (c) further show whether the part is uniform inside. The microstructure of zone I and Zone II is dendritic with no obvious dif­ ference in microstructure. Aldalur et al. [56] also used GMAW-based WAAM technology to prepare the same mold, and the results showed a similar microstructure with a dendritic structure.  

To further study the microstructure of Invar 36 alloy manufactured by PAW-based and GMAW-based technology. Veiga et al. [54] investi­ gated the differences in the microstructure of the as-WAAMed Invar 36 alloy. As shown in Fig. 16, the microstructure of PAW and GMAW processes are similar, with traces of adjacent layer laps in the XZ plane and equiaxed and columnar crystals in the XY plane. The difference is that the lap layer morphology and grain distribution corresponding to the two processes are different, which is related to the different heat input amounts of the two processes [91].  

Furthermore, Sood et al. [81] studied the microstructures of GATM-based WAAM Invar 36 alloy at different process parameters, as shown in Fig. 17. The microstructure consists of epitaxial columnar grains and cellular structures under varying heat input conditions were observed in Fig. 17(a) and (b). Then, with increasing heat input from $220~\mathrm{\J/mm}$ to $550~\mathrm{~J/mm}$ , the microstructure gradually coarsens, potentially attributed to a reduction in nucleation rate caused by higher heat input, resulting in larger grain size [92]. The large heat input also easily leads to the formation of cracks. As shown in Fig. 17(d–f), cracks are easy to form at the high angle grain boundary (HAGB), which is due to the large accumulated thermal stress at the HAGB (The KAM value at HAGB is larger in Fig. 17(f).). However, it should be noted that no cracks were observed at low heat input in Fig. 17(c–e). Sood et al. [81] emphasized that crack is not attributed to solidification cracking or challenges in material formation, as evidenced by the absence of trace elements such as P and S at the crack site and the absence of cracks under low heat input conditions.  

# 3.2.5. Microstructure of as-DEDed Invar 36 alloy  

Fig. 18 depicts the macrostructure of Invar 36 alloy produced by DED technology, where an equiaxial region with a height of approximately $250~{\upmu\mathrm{m}}$ is observed at the top [69], which is also evident in other ma­ terials such as titanium alloy [93]. The as-DEDed specimen appears columnar grain morphology throughout; however, the size of grains decreases from top to bottom. Minor columnar grains are visible at the bottom amidst stratified equiaxed grains. According to Fig. 19(a), (b), and (c), it is apparent that the direction of columnar grain growth de­ viates from the deposition direction. One-way laser scanning (OLS pattern), results in consistent growth while back-and-forth laser scan­ ning (BFS pattern), forms a $^{*}Z^{\dprime}$ shape [69].  

Fig. 19(d–h) shows the structure of as-DEDed specimens and differ­ ences in grain growth caused by laser scanning. The temperature gradient $(G_{L})$ is crucial for determining grain morphology during deposition in Fig. 19(h). The formation of columnar grain can be analyzed according to the following Eq. (1) [94]:  

$$
G_{L}>0.617(100N_{0})^{\frac{1}{3}}\left[1-\left(\frac{\Delta T_{N}}{\Delta T c}\right)^{3}\right]\Delta T_{c}
$$  

$N_{0}$ is the overall density of dissimilar substrate particles within a given volume, $\Delta T_{N}$ is the degree of undercooling of nucleation, and $\Delta T_{C}$ is the degree of undercooling of columnar grain.  

According to Eq. (1), if the local subcooling at the crystallization front exceeds the nucleation cooling rate, middle grains in the melt pool will initiate nucleation and cause columnar equiaxial transition (CET). At the bottom of the melt pool, heat dissipation through unmelted particles and the surrounding atmosphere triggers CET and the forma­ tion of equiaxed grains due to a critical temperature gradient [95]. Heat dissipation during deposition occurs through conduction, convection, and radiation. Conduction via the substrate is the most efficient method. The laser scanning process creates a molten pool that cools rapidly upon contact with the matrix material, resulting in short solute diffusion time.  

![](images/05fc5ebd7a9c9beeae36820dca99a186d553e4c9bfcca96733ec0b003a885acd.jpg)  
Fig. 19. Microstructure characteristics of as-DEDed specimens: (a, c) columnar grain orientation, (d) laser scanning strategy, and (d–f) microstructures evolution of equiaxed, cellular, and columnar grains. Additionally, $(\mathbf{f-g})$ illustrates the difference between OLS and BFS deposition patterns while (h) shows the temperature gradient during deposition [69].  

![](images/f044ab6e8c415b765d6b4f1b9c5164d8d9a63b921fc0f4ec6117406ebfcb51fa.jpg)  
Fig. 20. Microstructure of single molten pool in as-DEDed Invar 36 alloy: (a) optical microscope, (b) simulative microstructure simulation results [98]  

Due to the rapid cooling, a significant temperature gradient is generated, resulting in an imbalanced microstructure with small columnar grains, as shown in Fig. 19(d).  

In the solidification process, the heat of the molten pool flows first to the solidification zone and then to the matrix [96]. The size and direc­ tion of $G$ (temperature gradient) in a single molten pool are different [97]. Because $G$ in the stratified zone is lower than the critical gradient $G_{0}$ , a transition from columnar grains to honeycomb grains occurs. Upon layer deposition, the temperature gradient decreased significantly, resulting in a transition from columnar grains to an increasing number of cellular grains. Additionally, elongated cellular grains were observed as depicted in Fig. 19(e). Finally, the distinct arrangement of columnar grains and cell grains was formed. The columnar grains at the top layer (in Fig. 19(f)) are larger compared to those in the middle and bottom regions, while fewer cell grains are observed at the uppermost layer.  

In addition to the microstructures with multiple layers, the evolution of the melting pool in as-DEDed Invar 36 alloy within a single layer was also investigated [98]. Fig. 20 shows the actual single molten pool microstructure of as-DEDed Invar 36 alloy and the results obtained by the CA-FE model (three-dimensional cellular automaton-finite element method [99]). According to the experimental result in Fig. 20(a), the bottom of the molten pool is filled by the epitaxial growth of columnar grains, and the orientation of the columnar grains is consistent with the direction of the maximum temperature gradient in the molten pool. Moreover, the top of the molten pool is occupied by equiaxed grains. The simulation results are presented in Fig. 20(b), demonstrating a high level of consistency between the experimental and simulated outcomes. This suggests that exploring the intricate microstructure evolution of Invar alloy using the CA-FE model is indeed a viable approach.  

Furthermore, the impact of the SLS technology on manufacturing quality has only been preliminarily investigated and no reports have been made regarding its microstructure [46]. Currently, the macro and microstructure of AM-fabricated Invar 36 alloy exhibit a non-equilibrium solidification structure like that observed in another AM-fabricated alloy. However, certain phenomena associated with AM-fabricated Invar 36 alloy remain inadequately elucidated. Qiu et al. [21] reported that the proportion of bcc- $\upalpha$ phase in as-LPBFed Invar 36 alloy was $6.5\%$ based on the EBSD diagram, whereas Yang et al. [80] reported a value of $0.5\%$ . Further research is needed to investigate whether there is bcc- $\mathbf{\alpha}_{\cdot\upalpha}$ in other processes of AM-fabricated Invar 36  

G. Huang et al.  

![](images/32cd707bd3f1af53bb92e7995b27c93d1137759baed273a4159d2a7e0bc8b950.jpg)  
Fig. 21. OM micrograph shows the microstructure of Invar 36 alloy: (a) as-LPBFed specimen $(1000\mathrm{mm}/s)$ , (b)as-LPBFed $\mathrm{\Omega}_{\mathrm{(1000~mm/s)}}$ ) $^+$ heat treated specimen; (c) as-LPBFed $3200\ \mathrm{mm}/s)$ $^+$ HIPed specimen; (d) as-LPBFed $(3200\mathrm{\mm}/s)$ ) $^+$ HIPed $^+$ heat treatment specimen [21].  

![](images/28238b87475a5d77288dc0a8e8e28ed94ca7be26cef44314ab9b942c83744c1c.jpg)  
Fig. 22. Heat-treated (at $800^{\circ}C$ for $^{4\mathrm{h}}$ ) specimen EBSD diagram of Invar 36 alloy: (a–b) $\mathbf{N}_{2}$ -sprayed, (c–d) He-sprayed; (a, c) inverse pole figures (IPF), and (b, d) grain boundary maps [59].  

alloy, as well as the formation and content control of bcc- $\mathbf{\nabla}\cdot\mathbf{\vec{a}}$ , and the impact of these factors on properties. TEM is the most effective method for characterizing the bcc- $\mathbf{\nabla}\cdot\mathbf{\vec{a}}_{} $ phase due to the limitations of XRD, SEM, and EBSD.  

# 3.3. Microstructure after heat treatment  

The inherent rapid heating and cooling characteristics of metal ad­ ditive manufacturing processes result in the accumulation of nonuniform microstructures and internal stresses [100], necessitating post-treatment heat treatments to modify the microstructure or relieve residual stresses for comparable or superior properties compared to conventional fabrication [101]. Fig. 21 demonstrates the microstructure of the as-LPBFed specimens after post-treatment (Heat treatment: 830 ${}^{\circ}C/0.5\mathrm{h}$ , water quenching, $570~^{\circ}C/1\mathrm{h}$ , air cooling, $95~^{\circ}C/48\mathrm{h}$ . HIP process: $950~^{\circ}C/100~\mathrm{MPa/2h})$ [21]. Compare Fig. 21(a) and (b), and Fig. 21(c) and (d), respectively, there is no significant change in grain size and microstructure after HIP and/or heat treatment. Wegener et al. [73] also found a similar phenomenon.  

All specimens are dominated by vertical columnar grains and fanshaped columnar crystals with a few equiaxed grains in Fig. 21. The absence of any microstructural changes following heat treatment can be elucidated by analyzing the Fe–Ni alloy phase diagram [102]. The Invar 36 alloy begins to undergo phase transformation only at about $400^{\circ}C$ . Until then, it is the fcc-γ phase, after which the bcc- $\mathbf{\nabla}\cdot\mathbf{\vec{a}}_{} $ phase appears, but the phase content is small and almost difficult to observe (less than $5\%$ ) [103].  

![](images/3b4f5553aa177b9840fcb2d55664670bb03bd0cecf44eed4f4602eaf9a05862e.jpg)  
Fig. 23. Microstructure of Invar 36 alloy manufactured by WAAM technology at different conditions: (a, c) as-WAAMed condition, (b, d) heat-treated con­ dition. (a) and (b) are SEM pictures, (c) and (d) are EBSD pictures [71].  

![](images/6c93ff6ad6168de21219bd32cc5f166f54f9ffb008e59ff7a9b773ec519e6832.jpg)  
Fig. 24. Mechanical properties of the AM-fabricated Invar 36 alloy.  

Different from the LPBF technology, the microstructure changes of as-CSAMed specimens after heat treatment become obvious. As shown in Fig. 22, the grain size (in Fig. 22(a) and (c)) and boundary angle (in Fig. 22(b–d)) after heat treatment have obvious changes compared with that in Fig. 12. Specifically, static recrystallization occurs after heat treatment, stress is released, grain growth becomes equiaxed, and many annealed twins appear inside the grain, and large angular grain boundaries dominate.  

The microstructure of the Invar 36 alloy containing Niobium (Nb)  

manufactured by WAAM technology before and after heat treatment is illustrated in Fig. 23 [71]. The phase distribution of as-WAAMed Invar 36 alloy exhibits a honeycomb or network pattern in Fig. 23(a), while the grid particles appear coarse and discontinuous after heat treatment in Fig. 23(b). The volume fraction of the phase before and after the heat treatment is $2.39\%$ and $2.40\%$ respectively, which is difficult to pre­ cisely distinguish due to resolution limitation. The microstructure re­ mains almost unchanged before and after heat treatment, as shown in Fig. 23(c) and (d), with both exhibiting columnar grains. Qiu et al. [21] also found the same phenomenon, that is, the microstructure of as-LPBFed Invar 36 alloy is almost unchanged after heat treatment.  

Qiu et al. [21] and Jiao et al. [71] showed that the microstructure evolution of as-LPBFed and as-WAAMed Invar 36 alloy is not significant after heat treatment, which has a minor effect on the mechanical properties. The main advantage of AM-fabricated Invar 36 alloy is its ability to achieve comparable properties without the need for heat treatment. Nevertheless, heat treatment is also important for residual stress release and better properties. The current heat treatment employed is the standard method, which has not been optimized spe­ cifically for additive manufacturing. Therefore, the microstructure evolution and characterization of nano-level precipitates in AM-fabricated Invar 36 alloy through heat treatment require further investigation.  

# 4. Properties  

# 4.1. Mechanical properties  

Fig. 24 shows the ultimate tensile strength (UTS) and elongation (EL) of AM-fabricated Invar 36 alloy in the literature, and it can be seen from the figure that only LPBF, CSAM, DED, and WAAM technology have been studied currently, and LPBF and DED technology are predominant. The strength of the AM-fabricated Invar 36 alloy is better than (DED technology: $\mathrm{UTS}=586\ \mathrm{MPa}$ , ${\mathrm{EL}}=39\%$ ; WAAM technology: $\mathrm{UTS}=464$ MPa, $\operatorname{EL}=49\%$ that of the commercial Invar 36 alloy after heat treatment (commercial Invar 36 alloy, $\mathrm{UTS}=448\ \mathrm{MPa}$ , $\mathrm{EL}=35\%$ [104]). It is evident that additive manufacturing has great potential compared to traditional manufacturing processes, and there is less cur­ rent research on heat treatment processes, which has attracted more interest.  

In addition to tensile properties, the consideration of fatigue prop­ erties holds equal significance for Invar 36 alloy. Wegener et al. [73] first studied the low-cycle fatigue behavior of the as-LPBFed Invar 36 alloy. Conducting low-cycle fatigue experiments by varying strain am­ plitudes and observed a decrease in fatigue life with an increase in the total strain amplitude $(\triangle\mathfrak{\varepsilon}/2)$ from $\pm0.35$ to $\pm0.65$ [73]. Fig. 25 shows the half-life hysteresis loops of Invar 36 alloy under diverse total strain amplitudes. The plastic strain increases with the $\bigtriangleup\mathfrak{E}/2$ in Fig. 25(a–c). However, there is no significant dispersion in stress amplitude and number of failure cycles for different tests at each strain level. The curves in Fig. 25 (d) show almost perfect Masing behavior, which is quite intriguing. Thus, the LPBF-prepared Invar 36 alloy exhibits good damage tolerance, while the fatigue properties of Invar 36 alloy man­ ufactured by other AM process remain unreported.  

Zhang et al. [66], were the first to study high cycle fatigue behavior of as-LPBFed Invar 36 alloy. The fatigue fracture curve is depicted in Fig. 26(a), while Fig. 26(b) presents a comparison between the K-T graph of fatigue strength prediction and the experimental value. The crack propagates when the stress intensity factor amplitude $(\triangle K)$ ex­ ceeds the critical threshold value $(\triangle K_{t h})$ . When $E\nu$ is $105.8~\mathrm{J/mm^{3}}$ and $185.3\mathrm{J/mm}^{3}$ , $\triangle K_{t h}$ is $13.86M P a\cdot$ $\sqrt{m}$ and $13.67M P a\cdot$ $\sqrt{m}$ respectively. The curves of crack extension area under both $E\nu$ almost overlap, and the turning point in the crack break zone is nearly unanimous in Fig. 26(a). The crack propagation zone under both $E\nu$ almost completely overlaps and there is a consensus on the turning point in the crack break zone in Fig. 26(a). The microstructure and defects induced by different process  

G. Huang et al.  

![](images/69919d5971fe21f649cef05e0af3e495aeea92644c6a4b60b80444c216e7cfca.jpg)  
Fig. 25. Half-life hysteresis loops of as-LPBFed Invar 36 alloy at diverse total strain amplitudes $(\triangle\varepsilon/2)$ : (a) $\pm0.35\%$ , $(\mathbf{b})\pm0.5\%$ , $(\mathrm{c})\pm0.65\%$ and (d) all half-life hysteresis loops drew in relative coordinates [73].  

![](images/7953a259953b8e59960c10ec63e12b0da5cba6104803001e54ded7bf8708577f.jpg)  
Fig. 26. (a) Fatigue crack propagation curves for as-LPBFed Invar 36 alloy at laser energy densities $(E\nu)$ of $105.8~\mathrm{J/mm^{3}}$ and $185.3~\mathrm{J/mm^{3}}$ are shown, while (b) the Kitagawa–Takahashi (K–T) graph predicts the fatigue strength in high cyclic loading [66].  

parameters, with $E\nu$ values of 105.8 and $185.3~\mathrm{J/mm}^{3}$ , do not suffi­ ciently affect $\varDelta K_{t h},$ crack propagation, and break behavior. A similar rule was observed in another alloy manufactured via additive manufacturing [39].  

The fatigue strength value of Invar 36 alloy can be predicted by Eq. (2) [66], as follows:  

$$
\sigma_{t h}=\sigma_{f}\sqrt{\frac{l}{l+l_{0}}}
$$  

There, $\sigma_{t h}$ of fatigue strength, $\sigma_{f}$ of is the maximum fatigue strength under appropriate LPBF process parameters, l of intrinsic crack length, and $l_{O}$ of intrinsic crack length when l tends towards zero. Eq. (2) yields the relationship curve of $\sigma_{{t h}}\mathord{-}l$ , enabling accurate prediction of fatigue strength $(\sigma t h)$ when crack length $(l)$ is known in Fig. 26 (b).  

![](images/ed9edf18f433bb8f4bb69cd1dc79487db0e2e106d71ab26b7cd3dc91229d5bb4.jpg)  
Fig. 27. Variations in $0.2\%$ proof stress per atomic $\%$ of alloying elements added in Invar 36 alloy (obtained from the data of Tsuda and Wang [105]).  

It is noteworthy that the mechanical properties of AM-fabricated Invar 36 alloy exhibit variations, which are closely associated with process parameters and alloying elements. Moreover, for Invar 36 alloy, the mechanical properties are particularly sensitive to the alloying ele­ ments [105]. The density of the manufactured alloy is high, and the differences in properties can be attributed to variations in the alloying elements present. Tsuda et al. [106] investigated the impact of different alloying elements on its tensile strength (the majority exists as carbides or intermetallic compounds of C, with the remainder in solid solution as elements in Fig. 27), and found that Ti, Cr, and V exhibit a weakening effect among various elements. The lattice distortion in Invar 36 alloy results from the difference in atomic radii between Fe and Ni. The greater the disparity in atomic radii between the added elements and Fe/Ni, the more pronounced lattice distortion occurs, resulting in an elevated level of resistance. In fact, Invar 36 alloy properties often result from a combination of alloying elements.  

Table 2 Powder component for LPBF technology.   


<html><body><table><tr><td colspan="5">Element(wt.%)</td><td rowspan="2">Elongation (%)</td><td rowspan="2">Tensile strength (MPa)</td><td rowspan="2">Ref.</td></tr><tr><td>Fe</td><td>Ni</td><td>C</td><td>Mn</td><td>other</td></tr><tr><td>Bal.</td><td>35.8</td><td>0.032</td><td>0.047</td><td>～</td><td>30</td><td>516</td><td>[108]</td></tr><tr><td>Bal.</td><td>35.9</td><td>0.05</td><td>一</td><td>～</td><td>47</td><td>445</td><td>[67]</td></tr></table></body></html>  

Table 3 Comparison of the mean CTE $(20\ ^{\circ}C\sim200\ ^{\circ}C)$ of common alloys.   


<html><body><table><tr><td>TF-manufactured alloya</td><td>CTE(×10-6/ °C)</td><td>Ref.</td></tr><tr><td>Invar 36</td><td>1.2</td><td>[110]</td></tr><tr><td>Ti-6Al-4V</td><td>9.0</td><td>[111]</td></tr><tr><td>Ti-13V-11Cr-3Al</td><td>9.9</td><td>[108]</td></tr><tr><td>316 stainless steel</td><td>17.3</td><td>[112]</td></tr><tr><td>Hastelloy X</td><td>13.5</td><td>[112]</td></tr></table></body></html>

a Here, TF denotes the traditional fabricating process which normally includes casting, thermo-mechanical machining, and heat treatment.  

Table 2 shows the composition of the Invar 36 alloy powder for the LPBF technology, and the tensile strength of the alloy with the addition of the Mn element is higher, and the strength even reaches the perfor­ mance of the commercially annealed Invar 36 alloy. The addition of the right number of tiny elements (solid solution strengthening), together with the grain refinement (grain boundary strengthening) produced during the LPBF technology, will directly prepare Invar 36 alloy with excellent properties, omitting the heat treatment process, which is very attractive. In addition, Eissel et al. [107] reported that the addition of Zr and Hf elements to the Invar 36 alloy manufactured by the WAAM technology can slightly improve the hardness.  

The heat treatment has minimal impact on the mechanical properties [68] of AM-fabricated Invar 36 alloy and can even improve the coeffi­ cient thermal of expansion [108] or decrease tensile properties [21]. The current heat treatment process used is standard and does not meet the specific requirements of additive manufacturing. The current standard heat treatment is used to heat treat alloys. Hence, the regulation of mechanical properties through heat treatment lacks research. The me­ chanical properties of Invar 36 alloy manufactured under the same ad­ ditive manufacturing process parameters or from the same sample but at different positions exhibit significant dispersion, which poses a consid­ erable challenge for their practical application in engineering (such as in LPBF technology [66] and DED technology [69]). By controlling the wind field, atmosphere, and quality of raw materials during the printing process, dispersion can be further reduced without considering experi­ mental errors and random distribution of defects. Additionally, it is crucial to investigate the anisotropic mechanical properties and under­ lying mechanisms of AM-fabricated Invar 36 alloy for its engineering applications.  

# 4.2. Thermal expansion properties  

Invar 36 alloy is widely recognized for its remarkably low coefficient of thermal expansion (CTE) [109]. The CTE among common alloys is compared in Table 3. The CTE of Invar 36 alloy is only $1.2\times10^{-6}/{}^{\circ}C$ $(20~^{\circ}C\cdot200~^{\circ}C$ [110]), significantly lower than that of other alloys. While additive manufacturing offers numerous advantages, it is crucial to maintain a low CTE in Invar 36 alloy.  

Table 4 shows the CTE of the current Invar 36 alloy manufactured by CSAM, WAAM, LPBF, DED, and LPBF technology. Other additive manufacturing processes, such as Invar 36 alloy manufactured by BJT and SLS technology, have hardly studied its coefficient of thermal expansion, which also needs to be further explored by scientists. Moreover, Table 4 also shows that the AM-fabricated Invar 36 alloy has low or negative expansion properties, and the CTE values meet the ASTMF1684 standard. It is noteworthy that the negative thermal expansion of the AM-fabricated Invar36 alloy is not fortuitous or an experimental anomaly. This phenomenon has been observed in both asCSAMed [59] and as-LPBFed [113] Invar 36 alloy. This special phe­ nomenon suggests that the AM process parameters may be adjusted to achieve near-zero or negative expansion in Invar 36 alloy across a wide temperature range in the future.  

The LPBF technology is a widely investigated and representative approach for additive manufacturing of Invar 36 alloy [115]. As depicted in Fig. 28, the CTE of the as-LPBFed alloy is contingent on laser energy density, with lower CTE observed under varying laser energy densities (in Fig. 28(c)) from $0^{\circ}C$ to $600^{\circ}C$ (in Fig. 28(a–b)) compared to those prepared by conventional processes.  

Here, there are two interesting phenomena worth paying attention to, one is why a low expansion coefficient can be obtained without heat treatment, and the other is why the thermal expansion coefficient is different with different laser energy densities. At present, it is mainly explained by the porosity and residual stress. Fig. 29 shows the rela­ tionship between CTE of Invar 36 alloy and 316 stainless steel manu­ factured by LPBF technology with laser energy density at the temperature of $50~^{\circ}C.$ It can be found that not only is the expansion coefficient of Invar 36 alloy related to the energy density, but a similar rule also appears in 316 stainless steel. The laser energy density in Fig. 29 influences the porosity, which results in the variation of CTE [76]. It is found in Fig. 29 that the low expansion coefficient at lower and higher laser energy densities. When the laser energy density reaches the critical value (Ec), the porosity of alloys is minimized, while their thermal expansion is maximized. It is reported that the voids within the alloy provide greater internal thermal expansion space for the sur­ rounding microstructure and show lower apparent CTE [83]. The results demonstrate that diverse printing parameters can be employed to  

Table 4 Comparison of CTE $(10^{-6}/{}^{\circ}C)$ between TF-annealed and AM-fabricated Invar 36 alloy.   


<html><body><table><tr><td rowspan="2">Process</td><td colspan="5">Temperature (°C)</td><td rowspan="2">Ref.</td></tr><tr><td>25~100</td><td>25~200</td><td>30~100</td><td>30~150</td><td>30~200</td></tr><tr><td>TF-annealed</td><td></td><td>２</td><td>1.25</td><td>1.84</td><td>/</td><td>ASTM F1684 [114]</td></tr><tr><td>CSAM</td><td>一 -7.39~2.08</td><td>-8.86~3.63</td><td>/</td><td>/</td><td>/</td><td>[59]</td></tr><tr><td>LPBF</td><td>/</td><td>1.72-1.86</td><td>/</td><td>/</td><td>/</td><td>[80]</td></tr><tr><td>LPBF</td><td>/</td><td>/</td><td>0.66</td><td>1.78</td><td>/</td><td>[68]</td></tr><tr><td>LPBF</td><td>/</td><td>/</td><td>-0.471</td><td>0.098</td><td>0.767</td><td>[108]</td></tr><tr><td>DED</td><td>1.92</td><td>/</td><td>/</td><td>/</td><td>/</td><td>[70]</td></tr><tr><td>WAAM</td><td>1.94</td><td>/</td><td>/</td><td>/</td><td>/</td><td>[56]</td></tr></table></body></html>  

G. Huang et al.  

![](images/b7cfc4a8a9e55b3d6990c777246c9d1c2c4a432b5268fb1bc29ecd9cd61ca696.jpg)  
Fig. 28. Thermal expansion value of as-LPBFed Invar 36 alloy under different laser energy densities: (a, b) coefficient of linear expansion,(c) coefficient of therma expansion ( $25\mathrm{-}200~^{\circ}C)$ [80].  

![](images/16b39118e9641c1ce2d6cd4894e8cdd3db63150a64d0da5b1217e52a8829f2e4.jpg)  
Fig. 29. Thermal expansion of (a) as-LPBFed Invar 36 alloy and (b) as-LPBFed 316 stainless steel specimens (at the temperature $50~^{\circ}C)$ [76].  

![](images/ab2cfd966364de5ffaacf7f09258faf64f63f6c437ed402688910f2ec66f1e27.jpg)  
Fig. 30. As-LPBFed Invar 36 alloy thermal expansion in both x-y and z test orientations for the stress-relieved and deposited states [108].  

Table 5 Current main views on the CTE of AM-manufactured Invar 36 alloy.   


<html><body><table><tr><td rowspan="2">Technology</td><td colspan="2">Low CTE</td><td colspan="2">Anisotropic CTE</td><td rowspan="2">Ref.</td></tr><tr><td>Yes/ No</td><td>Reason</td><td>Yes/ No</td><td>Reason</td></tr><tr><td>LPBF</td><td>Yes</td><td>Residual stress</td><td>Yes</td><td>Defects</td><td>[108]</td></tr><tr><td>LPBF</td><td>Yes</td><td>Defects, Ni evaporation</td><td>/</td><td>/</td><td>[80]</td></tr><tr><td>LPBF</td><td>Yes</td><td>/</td><td>Yes</td><td>Tensile property</td><td>[21]</td></tr><tr><td>LPBF</td><td>Yes</td><td>/</td><td>No</td><td>/</td><td>[113]</td></tr><tr><td>LPBF</td><td>Yes</td><td>/</td><td>No</td><td>/</td><td>[68]</td></tr><tr><td>LPBF</td><td>Yes</td><td>/</td><td>No</td><td>Magnetic properties</td><td>[120]</td></tr><tr><td>WAAM</td><td>Yes</td><td>/</td><td>Yes</td><td>Microstructure</td><td>[71]</td></tr><tr><td>WAAM</td><td>Yes</td><td>/</td><td>Yes</td><td>Residual stress</td><td>[81]</td></tr><tr><td>WAAM</td><td>Yes</td><td>/</td><td>No</td><td>/</td><td>[56]</td></tr><tr><td>CSAM</td><td>Yes</td><td>Residual stress</td><td>/</td><td>/</td><td>[59]</td></tr></table></body></html>  

achieve distinct porosity, thereby attaining the desired coefficient of thermal expansion (CTE).  

Fig. 30 illustrates the variation of the coefficient of thermal expan­ sion in x-y and z orientations for as-LPBFed Invar 36 alloy before and after residual stress relief. Obviously, the CTE is initially low in the as  

![](images/ff7391113a9c9756cf243101f3742b591ae7c92519732aa12d8b75c333984cb8.jpg)  
Fig. 31. Invar 36 alloy Ku-band diplexer made of Invar 36 alloy manufactured via LPBF technology [121].  

![](images/c5edeb8f76faaa49ef9480a4fe6768881dd30596ad22005e4c9643789f015b19.jpg)  
Fig. 32. (a) 3D-sand printed mold, (b) mold infiltrated with a polymer resin, (c) Invar 36 alloy cladded to PH13-8 stainless steel by DED technology [122].  

LPBFed state but significantly increases following stress release. Addi­ tionally, there exists anisotropy in the coefficient of expansion among stress relieved Invar 36 specimens, which exhibits a greater CTE following the process of stress relief. The thermal expansion is related to the crystal structure, and Invar 36 alloy is a face-centered cubic metal, and there is no anisotropy in the crystallography. Therefore, the low CTE of as-LPBFed Invar 36 alloy is likely to be caused by residual stress [108]. It is worth mentioning that the residual stress may not affect the lattice thermal expansion, but rather the thermal expansion by affecting the magneto-volume shrinkage, with almost no effect on the micro­ structure anisotropy [116]. The presence of voids and residual stresses significantly reduces the CTE of the material, which can result in negative expansion, as observed in CSAM [59]. This regulation of CTE through inherent characteristics of the manufacturing process holds great promise for future research and application.  

Anyhow, the CTE of AM-fabricated Invar 36 alloy is lower compared to the traditional manufacturing process. This AM process exhibits sig­ nificant advantages in terms of its thermal properties. However, certain issues still require clarification. Table 5 summarizes some of the main current ideas regarding the CTE of AM-fabricated Invar 36 alloy. Visible, for the reason of the low coefficient of thermal expansion and different building directions of AM process anisotropy is controversial. For example, Jiao et al. [71] suggested that the anisotropy of the CTE is related to the microstructure, while Sood et al. [81] suggested the opposite. In fact, Invar 36 alloy is classified as a soft magnetic alloy [117], and its “Invar effect” with low coefficient thermal expansion can be explained from a physics perspective [118], such as magnetism [119]. Rao et al. [119] posit that there exists a positive correlation be­ tween the CTE of Invar 36 alloy and the ratio (Ms/Tc) of saturation magnetization $(\mathbf{M}_{\mathrm{S}})$ to Curie temperature (TC). This provides a method to elucidate the presence of CTE anisotropy in the AM-fabricated Invar 36 alloy, specifically by evaluating the $\mathbf{M}_{\mathrm{S}}/\mathrm{Tc}$ value of the specimen along different orientations. Based on the above analysis, the team showed that the CTE of as-LPBFed Invar 36 alloy is isotropic at $0^{\circ}$ , $45^{\circ}$ and $90^{\circ}$ building orientations by measuring magnetic properties [120]. This method can also be further used to analyze the effect of heat  

![](images/09f94836f7c716b58acf84c22b360de1e8decfac463f7ab5175f0e3c25a4f715.jpg)  
Fig. 33. Compression process of the three-period minimal surface cell structure of Invar 36 alloy with a wall thickness of $0.6\ \mathrm{mm}$ [123].  

![](images/3d7a03fe8f8a25c2c562df19fac1003f61e744800b05482bf084297ebc3499b8.jpg)  
Fig. 34. Invar 36 alloy mold: (a) three-dimensional model, (b) perspective view, (c) mold building direction, and (d) solid mold.  

G. Huang et al.  

![](images/e5a96faccc930e6c38d768068219d58e7247452d59b35e84f869d3cd2a067ecb.jpg)  
Fig. 35. Invar 36 alloy for nuclear applications: (a) coupled moderator and inside structure [124], (b) moderator piping [124], (c) tensile specimen [14].  

![](images/a0ccaf398c81ca17e5f724da16c945dcb121bf9542421c8a53b1c03800f7867a.jpg)  
Fig. 36. Invar 36 alloy for aircraft applications: (a) Composite mold for welding, (b)Sikorsky Comanche helicopter, (c) Invar 36 alloy mold for the upper skin of the Sikorsky Comanche helicopter, (d) Comanche RAH-66 helicopter mold [6].  

treatment on CTE in the future (see in Fig. 30).  

# 5. Application prospect of AM-fabricated Invar 36 alloy  

The summary in Sections 4.1 and 4.2 indicates that additive manufacturing of Invar 36 alloy can achieve low CTE and mechanical characteristics comparable to those of the cast and annealed materials, which lays a solid foundation for fabricating manufactured precise mold materials. For instance, Aldalur et al. [56] utilized the WAAM technol­ ogy to fabricate aerospace tooling made of Invar 36 alloy (see Fig. 15 (a)). Furthermore, harnessing the inherent advantages of LPBF tech­ nology, Wen et al. [121] fabricated a Ku-band diplexer with exceptional thermal stability for satellite communication, as shown in Fig. 31. Maravola et al. [122] have reported cases of AM-fabricated mold ma­ terials, as shown in Fig. 32. The mold in Fig. 32(a) is printed using 3D sand and can achieve tight bonding when coated with polymer in Fig. 32 (b). In Fig. 32(c), low expansion and high strength composites are shown, which were prepared using the DED process. Additive manufacturing of Invar 36 alloy holds immense potential in engineering, rendering it a treasure. The research on Invar 36 alloy across various fields is depicted in Fig. 2, which also highlights the significant potential applications for AM Invar 36 alloy.  

Previously, our team utilized LPBF technology to fabricate light­ weight lattice structures, as shown in Fig. 33 [123]. It is found that the G structure has the best plateau stress $(55.2\ \mathrm{MPa})$ elastic modulus (3.29 GPa), specific stiffness $(1.49\mathrm{\GPa{\cdot}g^{-1}{\cdot}c m^{3}})$ , and energy absorption effi­ ciency $(\geq80\%)$ . By utilizing the optimal G structure, as depicted in Fig. 34, a specialized mold for aerospace composite materials was manufactured with a remarkable weight reduction of $45.8\%$ . This also indicates the potential for producing Invar 36 alloy components using LPBF technology.  

Currently, additive manufacturing of Invar alloy is in its early stages, with many engineering applications still being explored. Fig. 35(a–c) shows the application of Invar 36 alloy in nuclear engineering. Invar 36 alloy was welded with aluminum alloy or SS316L to produce pipes (in Fig. 35(b)) or tensile specimens in Fig. 35(c). The welding of the pipe poses challenges, and the bonding strength at the interface is relatively low [124]. Additive manufacturing is a viable approach for dissimilar metal connections [125]. For instance, the WAAM process was utilized to prepare a P91 steel - Inconel 740H bimetallic structure [126], whereas the LPBF process was used to prepare an AlSi1MgMn – $\mathrm{AlSi7Mg0.6}$ bimetallic structure [127]. The vast potential of nuclear components fabricated via additive manufacturing is apparent. Fig. 36 depicts the applications of Invar alloy in aircraft [6]. The composite mold, with its complex geometric structure, requires multiple processes such as welding and cutting for preparation. Additive manufacturing can achieve integrated molding, thereby increasing production efficiency. Moreover, additive manufacturing of Invar alloy is a promising field with wide-ranging applications in the future.  

![](images/cb70cae42c75a0f7648fde2f8d54645fb13e0c880c0473630ce56fa908c9d30b.jpg)  
Fig. 37. AM-fabricated X-Invar matrix composite design concept.  

# 6. Invar matrix composite materials  

For the past few years, the rapid development of metal matrix composite materials has led to the addition of strengthening phases (such as elements and particles) to enhance performance beyond that of pure metals or alloys. The combination of additive manufacturing with metal matrix composites holds huge potential for material preparation and industrialization. Additive manufacturing not only enhances the design flexibility of Invar 36 alloy but also enables the preparation of Invar-composite materials, making it advantageous for fabricating structurally complex and lightweight devices. When designing com­ posite materials, it is preferable to select materials with a low or nearzero CTE to minimize the risk of damage. Invar 36 alloy, which boasts an exceptionally low coefficient of thermal expansion, represents an ideal choice for metal matrix composites [128]. Studies have shown that Invar is suitable as a matrix material for composite materials [31].  

Fig. 37 shows a thought guide for the additive manufacturing of Invar 36 alloy composites. Due to the low CTE of Invar 36 alloy, multifunctional low-expansion composites can be obtained by com­ pounding it with other materials. There are three main ways to manu­ facture Invar 36 alloy composites: (i) Coating, e.g., by directed energy deposition, cold spray additive manufacturing, etc., to coat the surface of Invar 36 alloy with ${\mathrm{Cr}}_{3}{\mathrm{C}}_{2}{\mathrm{-}}{\mathrm{VC}}/{\mathrm{C}}{\mathrm{o}}$ [129], TiC [130], and Fe-based amorphous coatings [131] to increase wear resistance. (ii) Interface, for example, by directed energy deposition and other processes (single or multilayer gradient binding), combining MnCu alloy [52] with Invar 36 alloy to manufacture a low expansion and high damping composite, and combining Ti6Al4V alloy [51] with Invar 36 alloy to manufacture a low expansion and oxidation resistant composite. (iii) Fusion, for example, using processes such as LPBF technology to dope TiAl [110], SiC [132], TiC [133], WC [134], $\Upsilon_{2}\mathrm{O}_{3}$ [135] and $\mathtt{C u l o s n}$ [136] into Invar 36 alloy to manufacture low expansion, high strength and high hardness composites. Next, the benefits of additive manufacturing Invar 36 alloy composites are demonstrated by the three composite methods mentioned above.  

# 6.1. Invar 36 alloy composites bonded by coating  

Laser cladding, as one of the additive manufacturing processes of directed energy deposition, has great advantages in coating preparation [137]. Zou et al. [129] coated Invar 36 alloy with Co-based coatings of different contents (specimens to as components YN1, YN2, and YN3) by laser cladding (in Fig. 38 (a)). Through research, Zou et al. [129] found that the wear resistance and oxidation resistance of coatings with different contents were better than Invar 36 alloy, and the oxidation resistance of $\mathrm{Cr_{3}C_{2}/C o}$ coating was better (in Fig. 38(c)), while the wear resistance of VC/Co coating was better (in Fig. 38(b)).  

(a) Chemical compositions of powders used for laser cladding (wt%).  

![](images/ec8f13c5902d66a58cc7431e2e5e084ba7bb3da0e11eb2851c8dbcaa8dbf7b7a.jpg)  
Fig. 38. Co base coating Invar 36 alloy properties: (a) chemical composition of coating,(b) wear properties, (c) oxidation resistance [129].  

![](images/b279901e51983ba6473e77ff5f9f23035bb679025b604ddb01b829aae5437490.jpg)  
Fig. 39. Ti–6Al–4V/Invar 36 alloy gradient material: (a)schematic diagram, (b)as-deposited specimen, (c)composition gradient [51].  

![](images/4868d61764f6e7891de67a9f51bb07a420c0d039d5e98a166491d3587449936d.jpg)  
Fig. 40. MnCu/Invar 36 alloy gradient materials: (a)schematic diagram, (b)as-deposited specimen [52  

![](images/361e692b984b474d29981193f600068d13fbc1933ffc07a07ec3490b71d73ae4.jpg)  
Fig. 41. EBSD map at different positions in the as-DEDed MnCu/Invar com­ posite [52].  

# 6.2. Invar 36 alloy composites bonded by interface  

The directed energy deposition process is very suitable for preparing gradient composites or dissimilar materials [138]. Fig. 39 shows the Ti–6Al–4V/Invar 36 alloy gradient material manufactured by DED technology. It can be observed that the manufactured alloy has a good gradient effect in Fig. 39(b–c). Bobbio et al. [51] verified the phase distribution and feasibility of gradient materials through thermody­ namic calculations and experiments, which laid a foundation for further research on mechanical properties.  

Fig. 40 shows the MnCu/Invar gradient composites manufactured by DED technology [52]. Fig. 41 shows an EBSD diagram of the grain size distribution of different components, and Fig. 42 shows grain boundary distribution (a), KAM diagram (b), hardness (c), and strength (d). The gradient materials MnCu/Invar 36 alloy have different ratios and obtain different microstructures in Figs. 41 and 42(a) and (b)). The larger the ratio of content for Invar 36 alloy, the larger the grain size. Meanwhile, the grain boundary angles and local stress concentrations at grain boundaries are also different (in Fig. 42(b)), which further affects the properties (in Fig. 42(c)). The manufactured gradient material has a UTS of 357 MPa and an El of $5.7\%$ (in Fig. 42(d)). Although the properties are low, the figures (in Figs. 41 and 42(b) and (c)) further explain that the microstructure and properties can be further tuned by adjusting the gradient composition, reflecting that Invar 36 alloy gradient materials have important scope for development.  

![](images/69ad51bcfa470ecd529938ff05a16e508c930849c3b3de93a30f7c252ea65911.jpg)  
Fig. 42. As-deposited MnCu/Invar composite: (a) grain boundary distribution map, (b) KAM map, (c) hardness distribution, (d) tensile properties [52].  

# 6.3. Invar 36 alloy composites bonded by fusion  

Doped alloying elements or compounds are commonly used to enhance the properties of composites. The high laser energy density of the LPBF process facilitates the fusion of additives with the matrix for composite formation [139].Wei et al. [136] studied the fusion quality of LPBF-manufactured bimetallic Invar 36 alloy powder and $\mathtt{C u l o s n}$ powder (low laser absorption rate, high thermal conductivity, and low melting temperature) after mixing. The experimental and simulation results indicate that higher volume laser energy density leads to better fusion quality, although the properties have not been reported.  

Although Invar 36 alloy has a low expansion, its strength is not high, and the addition of TiAl particles (Ti–48Al–2Cr–2Nb) can improve its strength. Qiu et al. [110] added 1.5 wt $\%$ TiAl particles to Invar 36 alloy and found that the addition of TiAl had almost no effect on relative density and grain size, but the generated nano- $\cdot\gamma$ -TiAl (in Fig. 43(a)),  

G. Huang et al.  

![](images/85a1a64a5419cb152a884f25d45202ce5a0024d57364ab27c7da272cbc79afda.jpg)  
Fig. 43. TEM micrographs of as-LPBFed 1.5TiAl-Invar 36 alloy: (a)TiAl particle, $\mathrm{(b)Al_{2}O_{3}}$ particle, $\mathrm{(c)B_{2}}$ –NiTi phase, (d) $B_{19}^{'}$ -NiTi phase [110].  

![](images/2500828b29f97ad0ab1a4d24436195026967e8b4f3f7bc6f2cfb458e767c5013.jpg)  
Fig. 44. Thermal expansion measurement results for the as-LPBFed Invar 36 and as-LPBFed Invar 36-1.5TiAl specimens [110].  

$\mathrm{{Al}}_{2}\mathrm{{O}}_{3}$ (in Fig. 43(b)), and TiNi phases (in Fig. 43(c and d)) effectively impeded dislocation motion to improve the strength of Invar 36 alloy.  

It is worth emphasizing that although the addition of TiAl particles improves the mechanical properties, it also increases the CTE in Fig. 44. The same is true of TiC-Invar 36 composites when TiC is added. Fig. 45 shows the mechanical properties of Invar 36 alloy manufactured by DED technology with different TiC particle additions. With increasing TiC content, the strength (in Fig. 45 (b)) and hardness (in Fig. 45(a)) of the TiC-Invar 36 composite increase while its thermal expansion coefficient increases (in Fig. 45(d)) and elongation decreases in Fig. 45(c).  

The enhanced strength of Invar 36 alloy, resulting from the incor­ poration of TiAl [140] and TiC particles [141], can be attributed to the synergistic effects of second-phase strengthening and precipitation strengthening. Coefficient of thermal expansion $(\alpha_{C})$ of the composite is connected to the volume fraction of its two phases, which can be explained using Rule of Mixture and Turner model as Eq. (3) [142] and Eq. (4) [143]:  

$$
\alpha_{\/C}=\alpha_{m}V_{m}+\alpha_{p}V_{p}
$$  

$$
a_{c}=\frac{\alpha_{m}V_{m}K_{m}+\alpha_{p}V_{p}K_{p}}{K_{m}V_{m}+K_{p}V_{p}}
$$  

Here, $\alpha_{m}$ represents the coefficient of thermal expansion for the matrix material and $\alpha_{p}$ denotes that for the reinforcement and $\alpha_{c}$ is composite. Additionally, $V_{m}$ and $V_{p}$ refer to the volume fractions of matrix and reinforcement materials respectively, while $K_{m}$ and $K_{p}$ represent their respective volume moduli.  

If the $\alpha_{C}$ of the composite is not greater than that of the matrix, then Eq. (4) must be satisfied.  

$$
\alpha_{c}\leq\alpha_{p}
$$  

$$
V_{m}+V_{p}=1
$$  

Here, Eq. (6) can be obtained by combining Eq. (2-5).  

$$
\alpha_{m}\leq\alpha_{p}
$$  

To maintain or decrease the $\scriptstyle{\alpha_{C}}$ of a composite material, the rein­ forcement should have a lower or equal coefficient compared to the matrix (as shown in Eq. (6)) [144]. However, TiC and TiAl particles have higher CTE $(7.4\times10^{-6}/{}^{\circ}C$ [145] and $10.8\times10^{-6}/{}^{\circ}C$ calculated by JMatPro software, respectively) than Invar 36 alloy $(2\times10^{-6}/{}^{\circ}C)$ , so adding them will increase the $\alpha_{C}$ of Invar 36 alloy. It is a significant research challenge to enhance strengthen and maintain/reduce low coefficient of thermal expansion of Invar36 alloy composites.  

Currently, AM-fabricated multifunctional Invar matrix composites exhibit promising prospects. However, there are still several areas that necessitate further investigation. Presently, the coefficient of thermal expansion of Invar matrix composites remains high; therefore, wide research is required to explore the selection of doping materials to maintain or reduce this coefficient. Additionally, while Invar 36 alloy commonly serves as a base material for preparing composite materials, limited research has been conducted on utilizing alternative base ma­ terials with Invar alloy 36 as the doping material. Despite the increase in the CTE of Invar matrix composite material, it is possible to control the coefficient of thermal expansion by additive manufacturing.  

# 7. Conclusion and perspectives  

This paper presents a review of the current research status of additive manufacturing of Invar 36 alloy and composites and introduces the  

G. Huang et al.  

![](images/c9bc46935c9ded0cb5c4295a97611d3901d4d355a8170202172668ee085f69ea.jpg)  
Fig. 45. Effect of TiC addition on the properties of as-DEDed Invare6 alloy: (a)hardness, (b) tensile strength,(c)elongation,(d) coefficient of thermal expansion [133].  

microstructure, mechanical properties, and thermal expansion proper­ ties as well as applications of AM-fabricated Invar 36 alloy. The con­ clusions obtained are as follows: Although the additive manufacturing of Invar 36 alloy is in its infancy, the current study shows the suitability of additive manufacturing for Invar 36 alloy parts development and pro­ duction. The mechanical properties and thermal coefficient of expansion of AM-fabricated Invar 36 alloy are equivalent to those achieved by traditional manufacturing process. Multifunctional Invar matrix com­ posites can be manufactured by additive manufacturing, and it is diffi­ cult to maintain or reduce the CTE while improving the mechanical properties.  

Despite significant advancements in additive manufacturing of Invar 36 alloy, there still exist numerous technical gaps. Based on the under­ standing of the team, suggestions and prospects for future research are put forward:  

Materials. The properties, especially the CTE, of Invar 36 alloy are highly sensitive to elemental variations, and adjustment of its composition by machine learning, materials genome engineering, thermodynamic calculation can lead to multifunctional or high (medium) entropy alloy. When combined with additive manufacturing technology, this expands the range of achievable material properties. The minor elements addition and its impact on Invar 36 alloy needs further systematic study. Additionally, there is a research gap in additive manufacturing of Super Invar alloy and Kovar alloy, which are like Invar 36 alloy. For Invar 36 alloy com­ posites, the key challenge is selecting additive materials that enhance strength without compromising its low expansion properties.  

Processes. Additive manufacturing of Invar 36 alloy is currently focused on the laser powder bed fusion, while other processes have been less studied. Therefore, it is imperative to explore alternative additive manufacturing, such as directed energy deposition and cold spray additive manufacturing for large dimensional device repair, while employing binder jetting for intricate mold preparation. The Invar 36 alloy is highly suitable for additive manufacturing. Hence, the more advanced micro-LPBF, area printing, ultrasonic additive manufacturing, friction stir additive manufacturing, and intelligent micro-casting and forging additive manufacturing can also be considered in future applications.  

Microstructure. The current study on microstructure evolution of as-printed and heat-treated Invar 36 alloy needs further investiga­ tion, particularly regarding the limited understanding of $\upalpha$ -Fe phase evolution and its impact on properties. The microstructure and phase evolution of Invar 36 alloy requires additional material character­ ization methods. Invar 36 alloy serves as an exemplary material for investigating the progression of microscopic defects by in situ XCT and in the additive manufacturing process owing to its exceptional formability. Since the processing window is relatively large for Invar 36 alloy, fine-tuning AM process parameters and designing micro­ structure precisely can lead to lower or near-zero expansion Invar 36 alloy with excellent strength-toughness compatibility.  

Properties. As seen above, the mechanical properties and coefficient of thermal expansion of AM-fabricated Invar 36 alloy are comparable to those of conventional manufacturing processes. The low coeffi­ cient of thermal expansion and anisotropic of AM-fabricated Invar 36 alloy is still under ongoing research hotspot, lacking a thorough explanation at present. Determining whether AM-fabricated Invar 36 alloy exhibits anisotropy in its coefficient of thermal expansion is crucial for fabricating dimensionally stable components in three di­ mensions. It must be mentioned that the Process-StructureProperties relationship of Invar 36 alloy has not been fully estab­ lished yet, and further in-depth research is needed. Using machine learning or numerical simulation or other methods to study process parameters can reduce the coefficient of thermal expansion and even achieve near-zero or negative expansion. In addition to tensile, fa­ tigue, and thermal properties, other properties such as compressive, wear resistance, corrosion resistance, impact toughness, and ther­ moelectric properties also require further investigation based on the application scenario.  

• Applications. Thanks to the advantages of additive manufacturing, it is possible to manufacture Invar 36 alloy components with preci­ sion structure (optical instruments, satellite parts, clock, sensor, etc.), complex geometry (composite aerospace mold, jet combustion chamber components, lightweight lattice filter, etc.), repair parts (LNG cabin repair, etc.). Before applying additive manufacturing, it is necessary to consider the suitability of different processes for specific applications, such as using LPBF for small precision com­ ponents and DED for large component preparation and repair. In the future, additive manufacturing of Invar 36 alloy will aim for light­ weight properties and integration of superstructure and structurefunction elements. Team has used the laser powder bed to prepare aerospace molds as well as to try to prepare custom satellite com­ ponents. As seen, the applications for additive manufacturing of Invar 36 alloy can be further expanded from the original.  

# Declaration of competing interest  

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.  

# Acknowledgment  

The research received financial support from the Nuclear Power Institute of China (No. JG2022311) and the University Scientific Research and Innovation Team Program of Sichuan (No. HG2022173).  

# References  

[1] Guillaume CE. Invar and its applications. Nature 1904;71(1832):134–9. [2] Harner LL. Invar at 100 years. Adv Mater Process 1997;151(5):31–4. [3] Kul M, Akgul B, Karabay YZ. The relationship of hot and cold rolling processes with the structure and properties of invar 36. Mater Chem Phys 2023;295. [4] Menshikov AZ, Kazantsev VA, Valiev EZ, Podgornykh SM. Magnetovolume effect and longitudinal spin fluctuations in invar alloys, NATO advanced research workshop on itinerant electron magnetism - fluctuation effects & critical phenomena. 1997. p. 243–59. Moscow, Russia. [5] Ishikawa Yoshikazu. Physics and engineering applications of magnetism. Springer-Verlag; 1990. [6] Smith RJ, Lewis GJ, Yates DH. Development and application of nickel alloys in aerospace engineering. Aircraft Eng Aero Technol 2001;73(2):138–46. [7] Saito H, Fukamichi K, Wakaoka K. Propagation characteristics of ultrasonic waves in antiferromagnetic Cr-Fe-Mn Invar alloy. J Jpn Inst Metals 1976;40(2): 193–6. [8] Park WS, Chun MS, Han MS, Kim MH, Lee JM. Comparative study on mechanical behavior of low temperature application materials for ships and offshore structures: Part I-Experimental investigations. Mater Sci Eng, A 2011;528(18): 5790–803. [9] Lashmanov OU, Vasilev AS, Vasileva AV, Anisimov AG, Korotaev VV. Highprecision absolute linear encoder based on a standard calibrated scale. Measurement 2018;123:226–34.   
[10] Yang H-S, Kihm H, Moon IK, Jung G- Choi S-C, Lee K-J, Hwang H-Y, Kim S-W, Lee Y- ree-shel the effective athermalization of an IR optical syste   
[11] Kaabi Development of specific materials for the high electric vehicles. In: SF2M annual meetin   
[12] Barka Oxidation and emissivity of Invar 36 alloy oys Compd 2019;772:1003–16.   
[13] Nan JM, expansion invar alloy at elevated temperature ater ;114(1):36–40.   
[14] Teshigawara Harada Maekawa F, Futakawa M. Development of invar joint for hydrogen transfer line in JSNS. J Nucl Mater 2012;431(1–3): 212–7.   
[15] Abbasi SM, Morakabati M, Mahdavi R, Momeni A. Effect of microalloying additions on the hot ductility of cast FeNi36. J Alloys Compd 2015;639:602–10.   
[16] Wang C, Yuan S, Yao C, Feng Z. Study of the effect of W and Mo binary alloying on Fe-Ni36 invar alloy properties, 4th international conference on manufacturing science and engineering (ICMSE 2013), dalian. PEOPLES R CHINA; 2013. p. 290.   
[17] Prica CV, Neamtu BV, Marinca TF, Popa F, Sechel AN, Isnard O, Chicinas I. Synthesis of Invar 36 type alloys from elemental and prealloyed powders by mechanical alloying. Powder Metall 2019;62(3):155–61.   
[18] Nie Q, Chen G, Wang B, Yang L, Zhang J, Tang W. Effect of Invar particle size on microstructures and properties of the Cu/Invar bi-metal matrix composites fabricated by SPS. J Alloys Compd 2022;891.   
[19] Su Y, Yang X, Wu D, Meng T, Li W, Feng W, Vairis A. Optimizing welding sequence of TIG cross-joint of Invar steel using residual stresses and deformations. J Manuf Process 2023;105:232–45.   
[20] Zheng J-j, Li C-s, He S, Cai B, Song Y-l. Deformation behavior of Fe-36Ni steel during cryogenic (123-173 K) rolling. J Iron Steel Res Int 2016;23(5):447–52.   
[21] Qiu C, Adkins NJE, Attallah MM. Selective laser melting of Invar 36: microstructure and properties. Acta Mater 2016;103:382–95.   
[22] Zhao G, Huang C, He N, Liu H, Zou B. Preparation and cutting performance of reactively hot pressed TiB2-SiC ceramic tool when machining Invar36 alloy. Int J Adv Manuf Technol 2016;86(9–12):2679–88.   
[23] Gu D, Shi X, Poprawe R, Bourell DL, Setchi R, Zhu J. Material-structureperformance integrated laser-metal additive manufacturing. Science 2021;372 (6545):932.   
[24] Yin Y, Tan Q, Bermingham M, Mo N, Zhang J, Zhang M-X. Laser additive manufacturing of steels. Int Mater Rev 2022;67(5):487–573.   
[25] Dilberoglu UM, Gharehpapagh B, Yaman U, Dolen M. The role of additive manufacturing in the era of Industry 4.0, 27th international conference on flexible automation and intelligent manufacturing (FAIM). Modena: ITALY; 2017. p. 545–54.   
[26] Sing SL, Huang S, Goh GD, Goh GL, Tey CF, Tan JHK, Yeong WY. Emerging metallic systems for additive manufacturing: in-situ alloying and multi-metal processing in laser powder bed fusion. Prog Mater Sci 2021;119.   
[27] Ngo TD, Kashani A, Imbalzano G, Nguyen KTQ, Hui D. Additive manufacturing (3D printing): a review of materials, methods, applications and challenges. Compos B Eng 2018;143:172–96.   
[28] Gao W, Zhang Y, Ramanujan D, Ramani K, Chen Y, Williams CB, Wang CCL, Shin YC, Zhang S, Zavattieri PD. The status, challenges, and future of additive manufacturing in engineering. Comput Aided Des 2015;69:65–89.   
[29] Hu Y. Recent progress in field-assisted additive manufacturing: materials, methodologies, and applications. Mater Horiz 2021;8(3):885–911.   
[30] Tan C, Weng F, Sui S, Chew Y, Bi G. Progress and perspectives in laser additive manufacturing of key aeroengine materials. Int J Mach Tool Manufact 2021;170.   
[31] Obidigbo C, Tatman E-P, Gockel J. Processing parameter and transient effects on melt pool geometry in additive manufacturing of Invar 36. Int J Adv Des Manuf Technol 2019;104(5):3139–46.   
[32] Malakizadi A, Mallipeddi D, Dadbakhsh S, M’Saoubi R, Krajnik P. Post-processing of additively manufactured metallic alloys - a review. Int J Mach Tool Manufact 2022;179.   
[33] Volpato GM, Tetzlaff U, Fredel MC. A comprehensive literature review on laser powder bed fusion of Inconel superalloys. Addit Manuf 2022;55.   
[34] Zhang W, Chabok A, Kooi BJ, Pei Y. Additive manufactured high entropy alloys: a review of the microstructure and properties. Mater Des 2022;220.   
[35] Kotadia HR, Gibbons G, Das A, Howes PD. A review of laser powder bed fusion additive manufacturing of aluminium alloys: microstructure and properties. Addit Manuf 2021;46.   
[36] Song J, Chen J, Xiong X, Peng X, Chen D, Pan F. Research advances of magnesium and magnesium alloys worldwide in 2021. J Magnesium Alloys 2022;10(4): 863–98.   
[37] Minneci RP, Lass EA, Bunn JR, Choo H, Rawn CJ. Copper-based alloys for structural high-heat-flux applications: a review of development, properties, and performance of Cu-rich Cu-Cr-Nb alloys. Int Mater Rev 2021;66(6):394–425.   
[38] G. Coykendall, Additive manufacturing: processes and standard terminology..   
[39] Becker TH, Kumar P, Ramamurty U. Fracture and fatigue in additively manufactured metals. Acta Mater 2021;219.   
[40] DebRoy T, Wei HL, Zuback JS, Mukherjee T, Elmer JW, Milewski JO, Beese AM, Wilson-Heid A, De A, Zhang W. Additive manufacturing of metallic components - process, structure and properties. Prog Mater Sci 2018;92:112–224.   
[41] Li K, Yang T, Gong N, Wu J, Wu X, Zhang DZ, Murr LE. Additive manufacturing of ultra-high strength steels: a review. J Alloys Compd 2023;965.   
[42] Huang W, Yu H, Yin J, Wang Z, Zeng X. Microstructure and mechanical properties of k4202 cast nickel base superalloy fabricated by selective laser melting. Acta Metall Sin 2016;52(9):1089–95.   
[43] Li EL, Wang L, Yu AB, Zhou ZY. A three-phase model for simulation of heat transfer and melt pool behaviour in laser powder bed fusion process. Powder Technol 2021;381:298–312.   
[44] Pavlenko AN, Kuznetsov DV, Bessmeltsev VP. Heat transfer enhancement during pool boiling of nitrogen on porous coatings produced by selective laser melting/ sintering (SLM/SLS). J Eng Thermophys 2022;31(1):1–10.   
[45] Han Z, Cao WB, Lin ZM, Li JT, Feng T. Progress on rapid prototyping of ceramic parts by selective laser sintering. J Inorg Mater 2004;19(4):705–13.   
[46] Khanna N, Mistry S, Rashid RAR, Gupta MK. Investigations on density and surface roughness characteristics during selective laser sintering of Invar-36 alloy. Mater Res Express 2019;6(8).   
[47] Liu Y, Zhang J-x, Zhang L-j. Microstructure analysis of martensite stainless steel by directed energy deposition and uniform high hardness. J Mater Process Technol 2022;300.   
[48] Singh A, Kapil S, Das M. A comprehensive review of the methods and mechanisms for powder feedstock handling in directed energy deposition. Addit Manuf 2020; 35.   
[49] Babuska TF, Krick BA, Susan DF, Kustas AB. Comparison of powder bed fusion and directed energy deposition for tailoring mechanical properties of traditionally brittle alloys. Manuf. Lett. 2021;28:30–4.   
[50] Zhan X, Qi C, Zhou J, Liu L, Gu D. Effect of heat input on the subgrains of laser melting deposited Invar alloy. Opt Laser Technol 2019;109:577–83.   
[51] Bobbio LD, Otis RA, Borgonia JP, Dillon RP, Shapiro AA, Liu Z-K, Beese AM. Additive manufacturing of a functionally graded material from Ti-6Al-4V to Invar: experimental characterization and thermodynamic calculations. Acta Mater 2017;127:133–42.   
[52] Fan W, Zhang C, Tan H, Wang Y, Peng Y, Zhang F, Lin X, Huang W. Microstructures and mechanical properties of Invar/MnCu functionally graded material fabricated by directed energy deposition. Mater Sci Eng, A 2022;860.   
[53] Del Val AG, Cearsolo X, Suarez A, Veiga F, Altuna I, Ortiz M. Machinability characterization in end milling of Invar 36 fabricated by wire arc additive manufacturing. Journal of Materials Research and Technology-Jmr&T 2023;23: 300–15.   
[54] Veiga F, Su´arez A, Artaza T, Aldalur E. Effect of the heat input on wire-arc additive manufacturing of invar 36 alloy: microstructure and mechanical properties, weld. World 2022;66(6):1081–91.   
[55] Guo X, Li H, Xue P, Pan Z, Xu R, Ni D, Ma Z. Microstructure and mechanical properties of 600 MPa grade ultra-high strength aluminum alloy fabricated by wire-arc additive manufacturing. J Mater Sci Technol 2023;149:56–66.   
[56] Aldalur E, Suarez A, Veiga F. Thermal expansion behaviour of Invar 36 alloy parts fabricated by wire-arc additive manufacturing. Journal of Materials Research and Technology-Jmr&T 2022;19:3634–45.   
[57] Vargas-Uscategui A, King PC, Yang S, Chu C, Li J. Toolpath planning for cold spray additively manufactured titanium walls and corners: effect on geometry and porosity. J Mater Process Technol 2021;298.   
[58] Li W, Yang K, Yin S, Yang X, Xu Y, Lupoi R. Solid-state additive manufacturing and repairing by cold spraying: a review. J Mater Sci Technol 2018;34(3):440–57.   
[59] Chen C, Xie ${\mathrm{Y}},$ Liu L, Zhao R, Jin X, Li S, Huang R, Wang J, Liao H, Ren Z. Cold spray additive manufacturing of Invar 36 alloy: microstructure, thermal expansion and mechanical properties. J Mater Sci Technol 2021;72:39–51.   
[60] Petrackova K, Kondas J, Guagliano M. Fixing a hole (with cold spray). Int J Fatig 2018;110:144–52.   
[61] Mao Y, Li J, Li W, Cai D, Wei Q. Binder jetting additive manufacturing of 316L stainless-steel green parts with high strength and low binder content: binder preparation and process optimization. J Mater Process Technol 2021;291.   
[62] Sivarupan T, Balasubramani N, Saxena P, Nagarajan D, El Mansori M, Salonitis K, Jolly M, Dargusch MS. A review on the progress and challenges of binder jet 3D printing of sand moulds for advanced casting. Addit Manuf 2021;40.   
[63] Ziaee M, Crane NB. Binder jetting: a review of process, materials, and methods. Addit Manuf 2019;28:781–801.   
[64] Lores A, Azurmendi N, Agote I, Espinosa E, García-Blanco MB. A study of parameter and post-processing effects on surface quality improvement of Binder Jet 3D-printed Invar36 alloy parts. Progress in Additive Manufacturing 2022;7 (5):917–30.   
[65] Yang S, Yang Q, Qu Z, Wei K. Influence of manufacturing defects on mechanical behavior of the laser powder bed fused invar 36 alloy: in-situ X-ray computed tomography studies. Materials 2023;16(8).   
[66] Zhang C, Zhou Y, Wei K, Yang Q, Zhou J, Zhou H, Zhang X, Yang X. High cycle fatigue behaviour of Invar 36 alloy fabricated by laser powder bed fusion. Virtual Phys Prototyp 2023;18(1).   
[67] Wei K, Yang Q, Ling B, Yang X, Xie H, Qu Z, Fang D. Mechanical properties of Invar 36 alloy additively manufactured by selective laser melting. Mater Sci Eng, A 2020;772.   
[68] Rishmawi I, Rogalsky A, Vlasea M, Salarian M, Bakhshivash S. The effects of heat treatment on tensile and thermal expansion behavior of laser powder-bed fusion Invar36. J Mater Eng Perform 2022;31(12):9727–39.   
[69] Li H, Chen B, Tan C, Song X, Feng J. Microstructure evolution and mechanical properties of laser metal deposition of Invar 36 alloy. Opt Laser Technol 2020; 125.   
[70] Tan H, Wang Y, Wang G, Zhang F, Fan W, Feng Z, Lin X. Investigation on microstructure and properties of laser solid formed low expansion Invar 36 alloy. Journal of Materials Research and Technology-Jmr&T 2020;9(3):5827–39.   
[71] Jiao G, Fang X, Chen X, Xi N, Zhang M, Liu Y, Wu H, Huang K. The origin of low thermal expansion coefficient and enhanced tensile properties of Invar alloy fabricated by directed energy deposition. J Mater Process Technol 2023;317: 117994.   
[72] Heine B, Kah A, Sedlmajer M, Ocker C, Merkel M. Impact of corrosion on mechanical properties of additively manufactured Invar 36Einfluss von Korrosion auf die mechanischen Eigenschaften von additiv gefertigtem Invar 36. Mater Werkst 2022;53(3):316–27.   
[73] Wegener T, Brenne F, Fischer A, Moeller T, Hauck C, Auernhammer S, Niendorf T. On the structural integrity of Fe-36Ni Invar alloy processed by selective laser melting. Addit Manuf 2021;37.   
[74] Sanaei N, Fatemi A. Defects in additive manufactured metals and their effect on fatigue performance: a state-of-the-art review. Prog Mater Sci 2021;117.   
[75] Chen Y, Peng X, Kong L, Dong G, Remani A, Leach R. Defect inspection technologies for additive manufacturing. Int J Extrem Manuf 2021;3(2).   
[76] Yakout M, Elbestawi MA, Veldhuis SC. A study of thermal expansion coefficients and microstructure during selective laser melting of Invar 36 and stainless steel 316L. Addit Manuf 2018;24:405–18.   
[77] Mostafaei A, Zhao C, He Y, Ghiaasiaan SR, Shi B, Shao S, Shamsaei N, Wu Z, Kouraytem N, Sun T, Pauza J, Gordon JV, Webler B, Parab ND, Asherloo MD, Guo Q, Chen L, Rollett A. Defects and anomalies in powder bed fusion metal additive manufacturing. Curr Opin Solid State Mater Sci 2022;26(2).   
[78] Yakout M, Phillips I, Elbestawi MA, Fang Q. In-situ monitoring and detection of spatter agglomeration and delamination during laser-based powder bed fusion of Invar 36. Opt Laser Technol 2021;136.   
[79] Cabibbo M, Montanari R, Pola A, Tocci M, Varone A. Mechanical spectroscopy study of as-cast and additive manufactured AlSi10Mg. J Alloys Compd 2022;914.   
[80] Yang Q, Wei K, Yang X, Xie H, Qu Z, Fang D. Microstructures and unique low thermal expansion of Invar 36 alloy fabricated by selective laser melting. Mater Char 2020;166.   
[81] Sood A, Schimmel J, Ferreira VM, Bosman M, Goulas C, Popovich V, Hermans MJM. Directed energy deposition of Invar 36 alloy using cold wire pulsed gas tungsten arc welding: effect of heat input on the microstructure and [82] Hou Yi C, Jianzhao W, Xinzhi W, Wentao Y. Process parameter optimization of metal additive manufacturing: a review and outlook. Journal of Materials Informatics 2022;2(4):16. [83] Asgari H, Salarian M, Ma H, Olubamiji A, Vlasea M. On thermal expansion behavior of invar alloy fabricated by modulated laser powder bed fusion. Mater Des 2018;160:895–905. [84] Jing G, Wang Z. Influence of molten pool mode on microstructure and mechanical properties of heterogeneously tempered 300M steel by selective laser melting. J Mater Process Technol 2021;296. [85] Carter LN, Martin C, Withers PJ, Attallah MM. The influence of the laser scan strategy on grain structure and cracking behaviour in SLM powder-bed fabricated nickel superalloy. J Alloys Compd 2014;615:338–47. [86] Miao G, Du W, Pei Z, Ma C. A literature review on powder spreading in additive manufacturing. Addit Manuf 2022;58. [87] Menon V, Aranas Jr C, Saha G. Cold spray additive manufacturing of copperbased materials: review and future directions. Materials Science in Additive Manufacturing 2022;1(No 2). Materials Science in Additive ManufacturingDO - 10.18063/msam.v1i2.12 (2022).   
[88] Elkaseer A, Chen KJ, Janhsen JC, Refle O, Hagenmeyer V, Scholz SG. Material jetting for advanced applications: a state-of-the-art review, gaps and future directions. Addit Manuf 2022;60.   
[89] Fang X, Zu Y, Ma Q, Hu J. State of the art of metal powder bonded binder jetting printing technology. Discover Mater 2023;3(1):15. [90] Lin Z, Song K, Yu X. A review on wire and arc additive manufacturing of titanium alloy. J Manuf Process 2021;70:24–45. [91] Veiga F, Suarez A, Aldalur E, Artaza T. Wire arc additive manufacturing of invar parts: bead geometry and melt pool monitoring. Measurement 2022;189.   
[92] Wang FZ, Zhang CH, Cui X, Zhou FQ, Zhang S, Chen HT, Chen J. Effect of energy density on the defects, microstructure, and mechanical properties of selectivelaser-melted 24CrNiMo low-alloy steel. J Mater Eng Perform 2022;31(5): 3520–34. [93] Wang T, Zhu YY, Zhang SQ, Tang HB, Wang HM. Grain morphology evolution behavior of titanium alloy components during laser melting deposition additive manufacturing. J Alloys Compd 2015;632:505–13. [94] Fu H, Liu L. Progress of directional solidification in processing of advanced materials. Materials Science Forum - MATER SCI FORUM 2005;475–479:607–12.   
[95] Yan F, Xiong W, Faierson EJ. Grain structure control of additively manufactured metallic materials. Materials 2017;10(11). [96] Zhang Q, Chen J, Lin X, Tan H, Huang WD. Grain morphology control and texture characterization of laser solid formed Ti6Al2Sn2Zr3Mo1.5Cr2Nb titanium alloy. J Mater Process Technol 2016;238:202–11. [97] Zhu Y, Liu D, Tian X, Tang H, Wang H. Characterization of microstructure and mechanical properties of laser melting deposited Ti–6.5Al–3.5Mo–1.5Zr–0.3Si titanium alloy. Mater Des 2014;56:445–53. 1980-2015.   
[98] Zhan X, Lin X, Gao Z, Qi C, Zhou J, Gu D. Modeling and simulation of the columnar-to-equiaxed transition during laser melting deposition of Invar alloy. J Alloys Compd 2018;755:123–34.   
[99] Zaeem MA, Yin H, Felicelli SD. Comparison of cellular automaton and phase field models to simulate dendrite growth in hexagonal crystals. J Mater Sci Technol 2012;28(2):137–46.   
[100] Liao S. Toward a digital twin of metal additive manufacturing: process optimization and control enabled by physics-based and data-driven models. 2023.   
[101] Elahinia MH, Hashemi M, Tabesh M, Bhaduri SB. Manufacturing and processing of NiTi implants: a review. Prog Mater Sci 2012;57(5):911–46.   
[102] Z. Kover, A. Roosz, Calculation of the equilibrium phase diagram of Fe-Ni alloy system by the ESTPHAD method, in: R. Roosz, M. Rettenmayr, Z. Gacsi (Eds.), Solidification and gravity Iv2006, pp. 609-614..   
[103] De Keyzer J, Cacciamani G, Dupin N, Wollants P. Thermodynamic modeling and optimization of the Fe-Ni-Ti system. Calphad-Computer Coupling of Phase Diagrams and Thermochemistry 2009;33(1):109–23.   
[104] Zheng S, Sokoluk M, Yao G, de Rosa I, Li X. Fe-Ni Invar alloy reinforced by WC nanoparticles with high strength and low thermal expansion. SN Appl Sci 2019;1 (2).   
[105] Tsuda M, Wang K. The effect of alloying elements on the mechanical properties of the Fe-36% Ni alloys. J Iron Steel Inst Jpn 1996;82(8):701–6.   
[106] Tsuda M, Wang K. The effect of alloying elements on the mechanical properties of the Fe- $36\%$ Ni alloys. Tetsu To Hagane-Journal of the Iron and Steel Institute of Japan 1996;82(8):701–6.   
[107] Eissel A, Engelking L, Gustus R, Treutler K, Wesling V, Schroepfer D, Kannengiesser T. Alloy modification for additive manufactured Ni alloy components—part I: effect on microstructure and hardness of Invar alloy. Weld World 2023;67(4):1049–57.   
[108] Harrison NJ, Todd I, Mumtaz K. Thermal expansion coefficients in Invar processed by selective laser melting. J Mater Sci 2017;52(17):10517–25.   
[109] Abberger SL. Advanced composite molds - a new use for Invar. International Symposium on the Invar Effect held on the Occasion of the 100th Anniversary of Its Discovery, Cincinnati, Oh 1996:317–25.   
[110] Qiu C, Liu Y, Liu H. Influence of addition of TiAl particles on microstructural and mechanical property development in Invar 36 processed by laser powder bed fusion. Addit Manuf 2021;48.   
[111] A.H. Committee, Properties and selection: nonferrous alloys and special-purpose materials, ASM International1990..   
[112] Gschneidner KA, Beaudry BJ, Capellen J. Properties and selection: nonferrous alloys and special-purpose materials. ASM International, Metals Handbook, Tenth Edit 1990;2:720   
[113] Hitzler L, Shahul Hameed MZ, Kah A, Merkel M, Werner E. Thermal expansion and temperature-dependent Young’s modulus of Invar fabricated via laser powder-bed fusion. Progress in Additive Manufacturing 2022;7(3):463–70.   
[114] ASTM F1684-06(2021), Standard specification for iron-nickel and iron-nickelcobalt alloys for low thermal expansion applications, https://www.astm.org/ f1684-06r21.html.   
[115] Akgul B, Kul M, Erden F. The puzzling thermal expansion behavior of invar alloys: a review on process-structure-property relationship. Crit Rev Solid State Mater Sci 2023;101:1–54.   
[116] Wang XL, Hoffmann CM, Hsueh CH, Sarma G, Hubbard CR, Keiser JR. Influence of residual stress on thermal expansion behavior. Appl Phys Lett 1999;75(21): 3294–6.   
[117] Wijn HPJ. Magnetic alloys for technical applications. Soft magnetic alloys, invar and elinvar alloys, magnetic alloys for technical applications. Soft magnetic alloys, invar and elinvar alloys. 1994.   
[118] Sahoo A, Medicherla VRR. Fe-Ni Invar alloys: a review. In: International conference on advanced materials behavior and characterization. Chennai, INDIA: ICAMBC); 2020. p. 2242–4.   
[119] Rao Z, Ponge D, Koermann F, Ikeda Y, Schneeweiss O, Friak M, Neugebauer J, Raabe D, Li Z. Invar effects in FeNiCo medium entropy alloys: from an Invar treasure map to alloy design. Intermetallics 2019;111.   
[120] Huang G, He $\mathrm{G},$ Liu Y, Huang K. Anisotropy of microstructure, mechanical properties and thermal expansion in Invar 36 alloy fabricated via laser powder bed fusion. Addit Manuf 2024;82:104025.   
[121] Wen X, Yu Y, Tian C, Guo C, Wu W, Li F, Li Y, Zhang A. An invar alloy SLM printed diplexer with high thermal stability. Ieee Transactions on Circuits and Systems Ii-Express Briefs 2022;69(3):1019–23.   
[122] Maravola M, Cortes P, Juhasz M, Rutana D, Kowalczyk B, Conner B, MacDonald E. Asme, Development of a low coefficient of thermal expansion composite tooling via 3D Printing. Pittsburgh, PA: ASMEInternational Mechanical Engineering Congress and Exposition; 2018. IMECE2018.   
[123] He G, Peng X, Zhou H, Huang G, Xie Y, He Y, Liu H, Huang K. Superior mechanical properties of Invar36 alloy lattices structures manufactured by laser powder bed fusion. Materials 2023;16(12).   
[124] Harada M, Teshigawa M, Maekawa F, Ooi M, Kasugai Y, Takada H. R&D of Invar duct for fabrication of 2nd JSNS moderators. J Nucl Mater 2014;450(1–3):104–9.   
[125] Liu FC, Dong P, Khan AS, Sun K, Lu W, Taub A, Allison JE. Amorphous interfacial microstructure and high bonding strength in Al-Fe bimetallic components enabled by a large-area solid-state additive manufacturing technique. J Mater Process Technol 2022;308.   
[126] Sridar S, Klecka MA, Xiong W. Interfacial characteristics of P91 steel-Inconel 740H bimetallic structure fabricated using wire-arc additive manufacturing. J Mater Process Technol 2022;300.   
[127] Dimatteo V, Liverani E, Ascari A, Fortunato A. Weldability and mechanical properties of dissimilar laser welded aluminum alloys thin sheets produced by conventional rolling and Additive Manufacturing. J Mater Process Technol 2022; 302.   
[128] Zweben C. 4.16 metal matrix composite thermal management materials. In: Beaumont PWR, Zweben CH, editors. Comprehensive composite materials II. Oxford: Elsevier; 2018. p. 386–96.   
[129] Zou Y, Ma B, Cui H, Lu F, Xu P. Microstructure, wear, and oxidation resistance of nanostructured carbide-strengthened cobalt-based composite coatings on Invar alloys by laser cladding. Surf Coating Technol 2020;381.   
[130] Wang HT, Zhang SQ, Huang JH, Zhu JL, Zhang H. Reactive detonation spraying of in situ synthesised TiC reinforced Fe36Ni based composite coatings via sucrose as carbonaceous precursor. Surf Eng 2009;25(4):295–302.   
[131] Zhai H, Li X, Li W, Cheng B, He D, Zhang X, Cui S. Strategy for improving the wear-resistance properties of detonation sprayed Fe-based amorphous coatings by cryogenic cycling treatment. Surf Coating Technol 2021;410.   
[132] Nagayama T, Yamamoto T, Nakamura T. Electrodeposition of invar Fe-Ni alloy/ SiC particle composite. In: Symposium on industrial electrochemistry and electrochemical engineering held during the PRiME joint international meeting of the electrochemical-society. Honolulu, HI: Electrochemical-Society-of-Japan, and Korean-Electrochemical-Society; 2016. p. 69–77.   
[133] Li XC, Stampfl J, Prinz FB. Mechanical and thermal expansion behavior of laser deposited metal matrix composites of Invar and TiC. Mater Sci Eng, A 2000;282 (1–2):86–90.   
[134] Prica C-V, Marinca TF, Neamtu BV, Sechel AN, Popa F, Jozsa EM, Chicinas I. Invar/WC composite compacts obtained by spark plasma sintering from mechanically alloyed powders. Materials 2022;15(19).   
[135] Du M, Wang L, Gao Z, Yang X, Liu T, Zhan X. Microstructure and element distribution characteristics of Y2O3 modulated WC reinforced coating on Invar alloys by laser cladding. Opt Laser Technol 2022;153.   
[136] Wei C, Gu H, Li Q, Sun Z, Chueh Y-h, Liu Z, Li L. Understanding of process and material behaviours in additive manufacturing of Invar36/Cu10Sn multiple material components via laser-based powder bed fusion. Addit Manuf 2021;37.   
[137] Lim WYS, Cao J, Suwardi A, Meng TL, Tan CKI, Liu H. Recent advances in lasercladding of metal alloys for protective coating and additive manufacturing. J Adhes Sci Technol 2022;36(23–24):2482–504.   
[138] Ansari M, Jabari E, Toyserkani E. Opportunities and challenges in additive manufacturing of functionally graded metallic materials via powder-fed laser directed energy deposition: a review. J Mater Process Technol 2021;294.   
[139] Essien U, Vaudreuil S. Issues in metal matrix composites fabricated by laser powder bed fusion technique: a review. Adv Eng Mater 2022;24(10).   
[140] Sun P, Qiu C. Influence of addition of TiAl particles on microstructural and mechanical property development in a selectively laser melted stainless steel. Mater Sci Eng, A 2021;826.   
[141] Zhao K, Gao T, Yang H, Hu K, Liu G, Sun Q, Nie J, Liu X. Enhanced grain refinement and mechanical properties of a high-strength Al-Zn-Mg-Cu-Zr alloy induced by TiC nano-particles. Mater Sci Eng, A 2021;806.   
[142] Duwe S, Arlt C, Aranda S, Riedel U, Ziegrnann G. A detailed thermal analysis of nanocomposites filled with SiO2, AlN or boehmite at varied contents and a review of selected rules of mixture. Compos Sci Technol 2012;72(12):1324–30.   
[143] Serebrennikov DA, Bykov AA, Trigub AL, Kolyshkin NA, Freydman AL, Aborkin AV, Tovpinets AO, Clementyev ES, Goikhman AY. Near zero thermal expansion in metal matrix composites based on intermediate valence systems: Al/ SmB6. Results Phys 2021;21:103843.   
[144] Zhou C, Zhou Y, Zhang Q, Meng Q, Zhang L, Kobayashi E, Wu G. Near-zero thermal expansion of ZrW2O8/Al-Si composites with three dimensional interpenetrating network structure. Compos B Eng 2021;211.   
[145] Wang H, Li Y, Xu G, Li J, Zhang T, Lu B, Yu W, Wang Y, Du Y. Effect of nano-TiC/ TiB2 particles on the recrystallization and precipitation behavior of AA2055-TiC TiB2 alloys. Mater Sci Eng, A 2023;871:144927.  

Dr. Ying Liu (Corresponding author 1) is an academic with a wealth of experience in the development and preparation of advanced metallic materials. He currently serves as the Dean of the School of Materials Science and Engineering at Sichuan University and is the director of the Engineering Laboratory of Rare Earth Vanadium and Titanium Functional Materials Preparation Technology of Sichuan Province. He is also the deputy director of the Key Laboratory of Advanced Special Materials and Preparation and Processing Technology of the Ministry of Education. Dr. Liu has been recognized as a na­ tional key expert, having led numerous national and provincial scientific research projects. He has been granted over 40 in­ vention patents and has published over 240 SCI papers in prestigious journals such as Nature Communications, Advanced Materials, Materials Science and Engineering: A, Scripta Materilia, Materials & Design, Corrosion Science, Materials Char­ acterization, International Journal of Refractory Metals and Hard Materials. Dr. Liu has been the recipient of multiple awards, including the National Technological Invention Award and the National Science and Technology Progress Award.  

![](images/fd4be0f40af549805fee44fd671c5c7f63e63fc11e1b324b79831736c671e350.jpg)  

Dr. Ke Huang (Corresponding author 2) obtained his Ph.D. in the United States from the University of Central Florida and currently works at the School of Materials Science and Engi­ neering, Sichuan University. He was a research engineer in Siemens Energy (US) and worked on additive manufacturing of materials and components development for over 10 years. Dr. Huang is currently a member of the ASTM F42 Additive Manufacturing International Standards Committee, partici­ pating in the development of more than ten international standards. He has published 12 SCI papers, holds 16 patents, and has been invited to speak at 20 international conferences.  

![](images/18e316ff9dee161d2eac0afa65fcad14a2f16698bbef3e4d19acd774252a3fc8.jpg)  

Dr. Guoliang Huang (first author) is pursuing a Ph.D in Ma­ terials Science at the School of Materials Science and Engi­ neering of Sichuan University. He received his master’s degree from Beijing University of Technology. His research interests are in the additive manufacturing of high-performance nickelbased superalloys, damping alloys, and low-expansion ironnickel alloys. He has authored 2 papers and obtained a patent for an innovative invention, the outcomes of which have been successfully implemented in both aircraft engines and marine shock absorbers.  

![](images/fa80238328e113ca11872630e54f0171127082749307b58cc05392020c73d604.jpg)  

G. Huang et al.  

![](images/c1848fb3b47056f2178900743213b84425035b071e264feee89263f665da1c3d.jpg)  

Dr. Gongming He obtained his Ph.D. degree from Sichuan University and currently serves as the Laboratory Adminis­ trator at the School of Materials Science and Engineering, Sichuan University.  

![](images/36fc3f044355216ebbbba656f9f5327cd26d9299beced9f5b7208cc76add0e3f.jpg)  

Dr. Yong He obtained his Ph.D. degree from Xi ’an Jiaotong University. He was a jointly trained Ph.D. student of the Technical University of Denmark and Xi’an Jiaotong Univer­ sity. His research interests are in the preparation and postprocessing of nuclear materials. He is currently employed as an assistant researcher at the Laboratory for Reactor Fuel and Materials in the Nuclear Power Institute of China, specializing in science and technology.  

![](images/c257354adba6416de1916e61067875193ffc5c14e90a5b20e2798fa32c816794.jpg)  

Dr. Xiufang Gong obtained her Ph.D. degree from Fudan University. The focus of her research lies in the development and fabrication of advanced materials specifically designed for application in gas turbines. She is serving as the deputy director of the State Key Laboratory of Clean and Efficient Turboma­ chinery Power Equipment.  