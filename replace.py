import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="alcateias-list grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6" style="max-width: 1200px; margin: 0 auto;">'
end_marker = '<!-- Fechamento Estratégico com CTA (Área de Destaque) -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print('Markers not found')
    sys.exit(1)

new_content = """<div class="alcateias-list grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6" style="max-width: 1200px; margin: 0 auto; width: 100%; box-sizing: border-box;">
  
  <div style="display: flex; flex-direction: column; gap: 1rem; width: 100%;">

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 01 (22 Págs.) | Introdução: Cantando sobre os ossos</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-summary"><strong>Resumo:</strong> O resgate da natureza instintiva feminina através da arqueologia psíquica. Compreendendo o parentesco com o feminino selvagem e os sintomas de uma alma faminta que foi soterrada pelo excesso de domesticação.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 02 (14 Págs.) | Capítulo 1 - O uivo: A ressurreição da Mulher Selvagem</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> La Loba, a Mulher-lobo / Os quatro rabinos</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> A lenda de La Loba, a mulher dos ossos no deserto. O processo laborioso de recolher os restos psíquicos dispersos e usar a voz da alma para cantar sobre os ossos, trazendo de volta à vida a nossa força indestrutível e vital. Com o acréscimo riquíssimo do conto 'Os quatro rabinos', que ilustra os diferentes destinos da mente humana ao entrar em contato com a imensidão do inconsciente, alertando para a necessidade de um ego estruturado para não se perder na iluminação ou no desespero.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 03 (36 Págs.) | Capítulo 6 - A procura da nossa turma: A sensação da integração como uma bênção</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> O patinho feio: a descoberta daquilo a que pertencemos / A rejection à criança diferente / Tipos de mães / O zigoto errado</p>
          <p class="alcateia-summary"><strong>Resumo Expandido:</strong> O reflexo psicológico do Patinho Feio e o arquétipo do proscrito. A cura da alienação e das feridas de rejeição familiar ao redescobrir a nossa verdadeira matilha e o clã ao qual pertencemos por direito de alma. Incorpora o mapeamento estrito das feridas do complexo materno através das cinco dinâmicas: a Mãe Ambivalente, que cede à pressão social sacrificando a cria; a Mãe Prostrada, exausta e incapaz de nutrir; a Mãe-Criança, ingênua e simplória diante da complexidade; e a Mãe Sem Mãe, órfã de amparo ancestral que vive no medo crônico da falha. Como contraponto clínico de resgate, desbravamos a força da Mãe Forte, que restaura o instinto selvagem e o verdadeiro alimento para a alma. O módulo culmina na libertadora metáfora do 'Zigoto errado', oferecendo um bálsamo terapêutico para quem cresceu sentindo-se um estranho no próprio ninho familiar, impulsionando o despertar da identidade legítima.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 04 (47 Págs.) | Capítulo 08 - A preservação do Self: A identificação de armadilhas, arapucas e iscas envenenadas</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> Os sapatinhos vermelhos / A mulher braba & A perda brutal nos Contos de Fadas / Atravessando as 8 armadilhas / Na casa do carrasco / O retorno à vida feita à mão, a cura dos instintivos feridos</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> A análise profunda de Os Sapatinhos Vermelhos. Como identificar e atravessar as armadilhas culturais e psíquicas que nos aprisionam em rotinas destrutivas, operando o retorno à vida feita à mão e a cura dos instintos feridos.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 05 (39 Págs.) | Capítulo 10 - As águas claras: O sustento da vida criativa</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> La Llorona / A menininha dos fósforos / Os três cabelos de ouro</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> O diagnóstico das obstruções na psique criativa e os métodos para limpar os canais obstruídos, devolvendo o fluxo vital e o sustento à imaginação, à arte e às águas puras da expressão pessoal. Trazendo em paralelo a dolorosa dinâmica de 'A menininha dos fósforos', que diagnostica o perigo de fantasiar em meio ao congelamento da alma, e as chaves de 'Os três cabelos de ouro' como caminhos de resgate da sabedoria oculta no próprio inconsciente.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 06 (37 Págs.) | Capítulo 2 - A tocaia ao intruso: O princípio da iniciação</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> O Barba-azul / O predador natural de psique / A chave do conhecimento: A importância de farejar / Como dar o Grito</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> O confronto com o predador natural da psique através do conto do Barba-azul. O amadurecimento da ingenuidade através do desrespeito à proibição de olhar: usando a chave do conhecimento para romper o entorpecimento e desarmar as forças destrutivas.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 07 (29 Págs.) | Capítulo 12 - A demarcação do território: Os limites da raiva e do perdão</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> O urso da meia-lua / As árvores ressecadas / Descansos</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> A canalização saudável e consciente da raiva instintiva como ferramenta de proteção territorial, compreendendo os limites compassivos do descanso e do verdadeiro perdão de si e do outro. Incorpora a metáfora das 'Árvores ressecadas' para compreender os ciclos de escassez criativa e afetiva, fundamentando a prática dos 'Descansos' como ritos indispensáveis de recolhimento para que a psique possa se regenerar e restabelecer seus limites naturais.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 08 (17 Págs.) | Capítulo 04 – O parceiro: A união com o outro</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> Manawee / Um hino para o Homem Selvagem: Manawee / A natureza dual das mulheres / A conquista da ferocidade / A mulher interior</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> O hino do Homem Selvagem através do conto de Manawee. O mistério e a beleza de desvendar a natureza dual das mulheres (as irmãs gêmeas da psique) e como o self instintivo e canino ajuda o parceiro a compreender e respeitar o feminino profundo.</p>
        </div>
      </div>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 1rem; width: 100%;">

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 09 (45 Págs.) | Capítulo 03 - Farejando os fatos: O resgate da intuição como iniciação</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> Vasalisa & BabaYaga / A Boneca no bolso: Vasalisa, a sabida / Elaboração das 9 tarefas</p>
          <p class="alcateia-summary"><strong>Resumo Expandido:</strong> A profunda jornada iniciática de Vasalisa, a sabida, rumo ao coração da floresta psíquica para encontrar a temível bruxa ancestral Baba Yaga. Este capítulo gigante destrincha cirurgicamente as 9 tarefas arquetípicas necessárias para a morte da submissão ingênua e aculturada, operando a transferência mística do poder para a boneca no bolso — o nosso instinto intuitivo herdado da linhagem materna. Investigamos o papel de Baba Yaga como a representação da natureza selvagem integradora que exige o tencionamento, a verdade e o trabalho manual da alma (como separar o trigo do restolho), ensinando a jovem loba a limpar os canais da percepção, a farejar as intenções ocultas e a utilizar o fogo da sabedoria instintiva para se posicionar com firmeza e autoridade no mundo prático.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 10 (12 Págs.) | Capítulo 11 - O cio: A recuperação de uma sexualidade sagrada</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> As deusas sujas / Baubo: A deusa do ventre / Coyote Dick / Uma viagem a Ruanda</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> A recuperação da sexualidade como uma força numinosa, vital e sagrada da psique feminina. Através das histórias das 'Deusas sujas' e da irreverência de 'Baubo: A deusa do ventre', resgatamos o poder do humor obsceno e curativo para libertar a energia psíquica estagnada pelo puritanismo social. O conto de 'Coyote Dick' traz a astúcia do trapaceiro (trickster) para desarmar a rigidez do ego, enquanto o doloroso relato de 'Uma viagem a Ruanda' funciona como um divisor de águas clínico, demonstrando como a reconexão com os instintos viscerais é o único caminho capaz de metabolizar traumas coletivos e sustentar a sobrevivência da alma diante do horror.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 11 (17 Págs.) | Capítulo 07 - O corpo jubiloso: A carne selvagem</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> La Mariposa, a Mulher-borboleta / O corpo nos contos de fadas / O poder das ancas</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> O corpo não como um objeto a ser moldado, mas como uma criatura viva com linguagem e sabedoria próprias. Através do mito de 'La Mariposa, a Mulher-borboleta', investigamos o corpo como o verdadeiro local de alquimia e transformação arquetípica, onde o envelhecimento e as curvas ganham dignidade sagrada. Analisamos a desmistificação do 'Corpo nos contos de fadas' para romper com as pressões estéticas patriarcais que adoecem a mente e resgatamos 'O poder das ancas' como símbolo ancestral de sustentação, fertilidade criativa e posicionamento firme da mulher sobre a própria terra.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 12 (47 Págs.) | Capítulo 09 - A volta ao lar: O retorno ao próprio Self</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> Pele de foca, pele da alma / A perda do sentido da alma como iniciação / A ecologia inata às mulheres</p>
          <p class="alcateia-summary"><strong>Resumo Expandido:</strong> O comovente e doloroso conto de 'Pele de foca, pele da alma', desvelando um dos maiores desafios da vida adulta: a perda sutil e gradual do sentido da nossa própria essência divina. Analisamos a dinâmica clínica de como o excesso de concessões cotidianas, obrigações rígidas e o distanciamento da nossa criatividade roubam a nossa 'pele' vital, gerando um rito de iniciação involuntário pelo sofrimento. Mapeamos a ecologia inata à psique e estruturamos o caminho técnico e inegociável de retorno cíclico ao lar espiritual — o mergulho nas águas profundas do inconsciente —, compreendendo que sem esse recolhimento para respirar e resgatar a própria pele, a alma adoece, definha e perde a capacidade de nutrir as suas escolhas autênticas.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 13 (14 Págs.) | Capítulo 13 - Marcas de combate: A participação no clã das cicatrizes</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> Os segredos como assassinos / A mulher dos cabelos de ouro / O capote expiatório</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> O perigo de manter segredos ocultos e o rito de integração ao 'clã das cicatrizes': transformando as marcas mais profundas de sofrimento passado em medalhas de sabedoria, cura e autoridade pessoal. Soma-se o diagnóstico clínico de como 'Os segredos agem como assassinos' silenciosos da vitalidade, utilizando 'A mulher dos cabelos de ouro' e o arquétipo do 'Capote expiatório' para ilustrar o processo de lançar luz sobre as sombras e romper pactos de silêncio.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 14 (40 Págs.) | Capítulo 05 - A caçada: Quando o coração é um caçador solitário</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> A mulher-esqueleto / Encarando a natureza de vida-morte-vida do amor / O coração como tambor e o canto para criar a vida / A dança do corpo e da alma</p>
          <p class="alcateia-summary"><strong>Resumo Expandido:</strong> O místico conto inuit da 'Mulher-esqueleto', investigando as complexas fases de reestruturação dos relacionamentos profundos e o verdadeiro significado do amor de devoção. Este capítulo monumental confronta o medo do ego em encarar a natureza de 'vida-morte-vida' das relações, demonstrando que o amor real exige a coragem de pescar e abraçar o que está morto, ferido ou desprovido de carne na história do outro e em nós mesmos. Estudamos o processo alquímico de transformar o coração em tambor através do choro e do canto que recriam a vida, desarmando os mecanismos de defesa e isolamento para que a alma possa dançar em comunhão sincera, permitindo o nascimento de uma intimidade madura, resiliente e despida de ilusões infantis.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 15 (75 Págs.) | Capítulo 14 - La Selva Subterrânea: A iniciação na floresta subterrânea</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> A donzela sem mãos / Desenvolvimento dos 7 estágios</p>
          <p class="alcateia-summary"><strong>Resumo Expandido:</strong> O mais longo, denso e complexo mapa de travessia clínica do livro: o grandioso mito de 'A donzela sem mãos'. Este módulo esmiúça detalhadamente os 7 estágios iniciáticos de isolamento, mutilação psíquica e regeneração no deserto pelos quais a alma passa ao romper com os pactos sombrios do patriarcado ou as barganhas do ego enfraquecido. Investigamos o doloroso percurso de caminhar pela floresta subterrânea sem o auxílio das 'mãos' práticas, forçando o desenvolvimento de uma visão espiritual e de uma paciência alquímica. É o tratado definitivo para compreender os longos ciclos de provação psicológica, demonstrando como as lágrimas conscientes operam o milagre do renascimento de membros inteiramente novos e o fortalecimento indestrutível do Self selvagem.</p>
        </div>
      </div>
    </div>

    <div class="alcateia-item">
      <button class="alcateia-header">
        <span class="alcateia-number-title">ALCATEIA 16 (17 Págs.) | Encerramento - Agir como sombra: Canto hondo, o canto profundo</span>
        <span class="alcateia-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </span>
      </button>
      <div class="alcateia-content">
        <div class="alcateia-content-inner">
          <p class="alcateia-subtitles"><strong>Subtítulos:</strong> As história como bálsamos medicinais / Os agradecimentos de Clarissa / A educação de uma jovem loba: uma bibliografia</p>
          <p class="alcateia-summary"><strong>Resumo:</strong> A integração final da jornada de atravessamento e as histórias como bálsamos medicinais para o indivíduo e para a comunidade. Orientações para a educação contânua de uma jovem loba na vida prática cotidiana. Incorpora de forma tocante 'Os agradecimentos de Clarissa', transformando as bênçãos finais da autora em um tratado prático de sustentação para a preservação da ecologia instintiva feminina.</p>
        </div>
      </div>
    </div>

  </div>
</div>
          </div>
        </div>

        <!-- Fechamento Estratégico com CTA (Área de Destaque) -->"""

final_content = content[:start_idx] + new_content + content[end_idx + len('<!-- Fechamento Estratégico com CTA (Área de Destaque) -->'):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print('Success!')
