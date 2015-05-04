__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"

from DungeonOfBlackCastle.Game.MasterScene import MasterScene
from Game.Game.MessageText import MessageText


class Scene1(MasterScene):
    commands = {'по правой дороге': 86, 'по левой': 110}

    def run(self):
        MessageText.add_text('В самое обыкновенное сказочное королевство приходит беда. В тихом лесу, на его южных границах, появляется хитрый и коварный волшебник Барлад Дэрт, в совершенстве овладевший искусством черной магии. Никто не знает, из каких земель он пришел. Вскоре окрестные жители начинают сторониться леса, который темные колдовские силы сделали таинственным и непроходимым, с множеством беспощадных ловушек и мерзких глубоких болот. Лес наводнили Гоблины и Орки — уродливые и жестокие воины Барлада Дэрта. А в самом центре леса, который теперь называют не иначе как Зачарованный лес, волшебник воздвиг Черный замок, и никому еще не удалось достичь его и безнаказанно вернуться обратно. Но волшебник не успокаивается на этом. Узнав, что во дворце живет прекрасная Принцесса — единственная дочь Короля — он посылает к ее отцу черных послов, чтобы просить ее руки. Гордый Король отказывает им, но послы появляются еще дважды. Каждый раз они спускаются с неба на могучих крылатых конях, и только Король может без страха смотреть им в глаза, столь большая и грозная сила исходит от них. Но Король непреклонен, хотя и понимает: Барлад Дэрт так просто не отказывается от своих намерений. И вот, когда послы в третий раз покидают дворец, Принцесса исчезает вместе с ними. Заклятие волшебника переносит ее в Черный замок, но она бесстрашно отказывается стать женой чародея, и тот, не в силах сдержать свою злобу, погружает ее в волшебный сон. По всему королевству герольды созывают смельчаков, обещая любую награду тому, кто освободит Принцессу. Один за другим покидают они столицу по Главному Южному тракту и исчезают в Зачарованном лесу. Но ни один не возвращается назад: Черный замок умеет беречь свои тайны. Хотите попытаться миновать западни Зачарованного леса, сразиться с беспощадными воинами Барлада Дэрта, проникнуть в Черный замок и разрушить колдовские чары? Если да, то собирайтесь в путь… \n Как и положено в сказках, путешествие начинается перед королевским дворцом. Узнав, зачем вы пришли, стражники провожают вас в Тронный зал, и вы предстаете перед Королем. Обрадованный тем, что есть еще в его королевстве герои, готовые рискнуть даже своей жизнью ради его дочери, он отправляет вас к придворному астрологу и волшебнику, лучшему в королевстве знатоку Белой магии — Майлину. Ведь вам придется сражаться не только с воинами, но и со злыми духами — без волшебства в дороге не обойтись. Однако даже Майлин не может предвидеть всего могущества Барлада Дэрта, да и времени на учебу у вас совсем мало. Он лишь успевает научить вас самым необходимым заклятиям и дать несколько советов. Вот заклятия, которые вы изучили: ЗАКЛЯТИЕ ЛЕВИТАЦИИ — с его помощью вы сможете подняться в воздух и перелететь то препятствие, которое вам встретится. Но будьте осторожны: заклятие действует не слишком долго, и если вы не рассчитаете свои силы, то можете опуститься на землю раньше, чем препятствие или опасность будут позади. ЗАКЛЯТИЕ ОГНЯ — поможет вам в нужный момент создать в воздухе огненный шар и направить его на врагов. Но в закрытых помещениях им надо пользоваться осмотрительно, чтобы не устроить пожар. ЗАКЛЯТИЕ ИЛЛЮЗИИ — вы создадите у вашего врага необходимую иллюзию и сможете спастись в тех ситуациях, из которых другого выхода не будет. Но заклятие иллюзии — опасное колдовство: ведь иллюзия рассеивается, и враг понимает, что его одурачили. ЗАКЛЯТИЕ СИЛЫ — прибавит вам силу и увеличит вашу СИЛУ УДАРА. ЗАКЛЯТИЕ СЛАБОСТИ — сделает вашего врага неуклюжим и неповоротливым, ослабит СИЛУ его УДАРА. ЗАКЛЯТИЕ КОПИИ — с его помощью вы сможете при случае создать точную Копию вашего противника, которую вы будете контролировать. Тогда прежде чем добраться до вас, ему придется драться с собственной Копией, МАСТЕРСТВО и ВЫНОСЛИВОСТЬ которой будут равны его МАСТЕРСТВУ и ВЫНОСЛИВОСТИ. Если ваш враг победит свою Копию, то с ним придется драться вам самим. Если же Копия сразит противника, то заклятие теряет силу и Копия исчезает, а вы продолжаете свой путь. Но если противников было несколько, а Копию вы смогли или захотели создать только одну, то придется драться и с остальными. ЗАКЛЯТИЕ ИСЦЕЛЕНИЯ — в любой момент (но не во время сражения) добавит вам 8 ВЫНОСЛИВОСТЕЙ. ЗАКЛЯТИЕ ПЛАВАНИЯ — вы никогда не видели ни реки, ни озера, а в дороге может случиться всякое. У вас уже нет времени учиться плавать. Но с помощью этого заклятия вы сможете переплыть любую водную преграду, которая вам встретится. Но будьте внимательны: как только вы ступите на землю, заклятие утратит свою силу. Астролог предупредил: уровень вашего МАСТЕРСТВА позволяет вам воспользоваться заклятиями только 10 раз. Майлин дает еще два совета. Во-первых, сориентироваться на запутанных лесных тропинках и в замке, если вы до него дойдете, вам поможет карта. Рисуйте ее по мере продвижения. Во-вторых, для многих магических таинств необходимы волшебные предметы. Старайтесь в своем путешествии добыть их как можно больше, при случае они помогут вам, но будьте осторожны: коварство врага не знает границ, возможны любые ловушки. После беседы с астрологом вы вновь предстаете перед Королем. Никто не знает, что вам может понадобиться на пути к успеху, поэтому из дворца вы берете с собой только самое необходимое: меч, флягу, заплечный мешок и 15 золотых. Король приказывает одному из герольдов проводить вас до границ Зачарованного леса, чтобы в пути вы не испытывали нужды ни в еде, ни в питье. По дороге вы спрашиваете герольда, кто такие Гоблины и Орки, о которых вы много слышали во дворце. Он рассказывает, что Гоблины — это страшные и отвратительные злые духи ростом примерно с человека, которые верой и правдой служат волшебнику. Их мало кто видел. И совсем уж никто и никогда не видел Орков. Говорят только, что они повыше и посильнее. Но и с теми и с другими лучше не встречаться. В пути вы еще раз обдумываете последний совет Майлина: Барлад Дэрт достаточно могущественный волшебник, чтобы даже малой частицы его мастерства, переданной особо преданным воинам, хватило не только на то, чтобы противостоять вашим заклятиям, но и наложить на вас свои, не менее быстрые и сильные. Будьте осмотрительны. Но вот королевским владениям приходит конец. Здесь надо спешиться: лес заколдован и не пускает всадника. Герольд прощается с вами, и вскоре лишь далекий стук копыт напоминает, что вы были не один. Черный, таинственный и неподвижный, Зачарованный лес ждет вас.\n')
        MessageText.add_text('Вы быстро идете вперед и вскоре оказываетесь в лесу. Даже странно, что о нем рассказывают столько страшных и невероятных историй: таинственный, зачарованный, с множеством ловушек и опасностей. Но все тихо и спокойно, высокие и могучие деревья справа и слева пропускают много солнечного света, дорога прямая и ровная, и вы расслабляетесь. Веселое щебетание птиц убеждает в том, что поблизости нет никакой опасности. Примерно через три четверти часа вы доходите до развилки. Путь раздваивается. Теперь вам надо принять первое решение — какую дорогу выбрать: [по правой дороге] или [по левой]?\n')