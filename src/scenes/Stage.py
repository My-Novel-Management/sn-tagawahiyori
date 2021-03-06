# -*- cofing: utf-8 -*-
'''
Stage: xxx
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_tagawa_biyori(w: World):
    asami = w.get("asami")
    eri = w.get('eri')
    man = w.get('man')
    return w.scene("田川日和",
            asami.do("教室の窓側を見やると温かな日差しが入り込んで眩しい"),
            asami.do("私は黒板に書かれた『山月記』というタイトルと、それに続く留め跳ねのしっかりとした箇条書きをノートに書き写しながら、もう一度窓際の彼の席を見やった"),
            asami.do("ぽつんと一つだけ空いている"),
            asami.do("田川昼男は今朝からずっといない。と言っても彼が不登校という訳ではない。事実昨日は登校してちゃんと苦手な数学の授業も聞いていた"),
            asami.do("田川がいない"),
            asami.do("けれどそのことに関して気にしているのは、どうやら自分だけだと気づいて、私は頬杖を突きながら何だか納得できない気持ちにとりあえず蓋をした"),
            w.br(),
            asami.do("休み時間になり、誰もが友達同士で集まってどうでも良い話で適当に盛り上がるのを見ながら、私は未だに馴染めない、真新しい野暮ったい紺のブレザーの青いタイを弄っていた"),
            eri.talk("ねえあさみん。アレ書いた？"),
            asami.do("後ろを振り返って訊いてきたのは、この数日で急に会話をするようになった足立衣里だ"),
            asami.talk("アレじゃ分かりません"),
            eri.talk("そういうのは適当に察していかないと、この田舎町じゃ生きてけないよ？"),
            asami.do("田舎、という言葉の響きが、どうしようもなく後ろに括った髪の房にぶら下がるようで、それに触れる度に私は気分が沈んでしまう"),
            eri.talk("ソレですよ、ソレ。ちゃんとあさみんの机の上にあるじゃない"),
            asami.do("言われて咄嗟に手で隠した印刷物には、進路予定表と書かれていた"),
            man.talk("そういや田川またか？"),
            asami.do("前の席に集まっている数人の男子生徒の声だ"),
            asami.do("彼の席をちらちらと見やりながら口元を同じように歪めて、へへら、みたいな笑い声を漏らしている"),
            asami.talk("あのさ"),
            asami.do("何も書いていない夕子の予定表を取り上げて眺めている衣里に、そんな田川昼男についてそれとなく訊いてみた"),
            asami.talk("みんな何も言わないの？"),
            eri.talk("あさみん知らないんだっけ？"),
            asami.do("足立衣里は目を細めて意味ありげに彼の席を見ると、私に視線を戻してからこう言った"),
            eri.talk("田川日和"),
            asami.talk("何それ"),
            eri.talk("やっぱりそうだよね。でも思い出してみてよ。田川君が今月に入って休んでる日ってさ……ほら、ね？"),
            asami.do("曜日、時間帯、その他にも何か共通項があったろうか。私は必死に思い出してみたが彼女が口にした言葉からある可能性に思い至った"),
            asami.talk("ひょっとして、天候？"),
            eri.talk("正解。ぜーんぶ天気良かった日でしょ？　だから田川日和なのよ"),
            asami.talk("でも田川君って、天気が良いから今日学校休みますっていう、その手の奇人だったっけ？"),
            eri.talk("あさみんは転校してきたとこだから知らないかもね。小学校の頃からそのあまりのマイペースさに当時の担任が命名したんだよ、田川日和って"),
            asami.do("その肝心の田川昼男は学校をサボってどこに居るのだろう"),
            )

def sc_bluesky(w: World):
    asami = w.get("asami")
    eri = w.get('eri')
    take = w.get('take')
    return w.scene("快晴",
            w.symbol("　　　　◆"),
            asami.do("翌日も驚くほどの快晴だった"),
            asami.do("だから今日も彼はいない。相変わらずの空席だ"),
            asami.do("男子は相変わらず田川日和と笑っている"),
            asami.do("でも誰一人として彼が何をしているのか知っていなかった"),
            asami.talk("ねえ足立さん"),
            eri.talk("なに？"),
            asami.talk("私も田川日和してもいいかな？"),
            eri.talk("あさみんってそういうキャラなの？！"),
            asami.do("足立さんは私をまじまじと眼鏡の奥の瞳を大きくして見つめるが、驚いているというよりもどこか楽しげで、腕組みをする動作をしてから教室を見回すと私に親指を立てて見せた"),
            eri.talk("代返なら任せろ"),
            asami.talk("大学じゃないから無理でしょ。けど、ありがと"),
            asami.do("そう言って足立さんに手を振ると、私は鞄を持って教室から抜け出した"),
            asami.do("授業開始のチャイムが鳴り響き、廊下にいた生徒たちがわっと各々の教室に駆け込んでいくが、私はそれを尻目に一階の通用口目掛けて思い切り走った"),
            take.talk("おい浅見。何か忘れ物か？"),
            asami.do("階段で竹村先生に見つかったが、"),
            asami.talk("良い日和なんで！"),
            asami.do("それだけ笑顔で答えると、白髪混じりの眉毛を凹ませた担任を放置して、階段の踊り場に思い切り飛び降りた"),
            )

def sc_paddyfield(w: World):
    asami = w.get("asami")
    tagawa = w.get('tagawa')
    granpa = w.get('granpa')
    return w.scene("トラクター",
            w.symbol("　　　　◆"),
            asami.do("自転車の前籠に鞄を投げ込んで漕ぎ出す。校門を出たところで校舎の方を見ると、見渡す限りが山に囲まれた場所なのだと実感できた"),
            asami.do("通りには車が渋滞しているようなこともなく、すれ違う車も小型のものや軽トラックが多い。トラクターがぶるぶるとエンジン音をさせて道路を走っていることだって珍しくないのだ"),
            asami.do("ほら、今だって前方をゆるゆる走っている真っ赤なトラクターが……"),
            asami.talk("あれ？"),
            asami.do("よく見れば特徴的な赤い野球帽は私の祖父だ"),
            granpa.talk("もう学校終わったのか？"),
            asami.talk("そうじゃないんだけど、説明が難しいからいいや。それよりじいちゃん。田川君見なかった？　こう、スポーツ刈りみたいな感じで丸顔の男の子なんだけど"),
            asami.do("自分で説明してみて、この辺りならどこにでもいそうな見た目をしているな、と改めて感じた。唯一違う点といえば、あの真っ直ぐ他人を見抜く鋭い瞳だろうか"),
            granpa.talk("田川んとこの坊主だろ？"),
            asami.talk("知ってるの！？"),
            granpa.talk("小学校の頃からの喧嘩仲間だよ。あいつとは昔っから反りが合わなくてなあ……どうにも顔見る度に口論になっちまう。それでもこの辺一帯を収める大地主様だろ？　口出ししたら親父にゲンコツされてなあ"),
            asami.do("またいつものように思い出話が始まりそうだったので、私はそれを遮《さえぎ》って尋ねる"),
            asami.talk("で、どこで見たの？"),
            w.br(),
            asami.do("自転車を漕ぐ足が筋肉痛になりそうだなと思いつつ、何とか坂道を登り終えるとその先にやっと目的の田んぼが広がっていた。それも一枚や二枚程度じゃなく、見渡す限り一面が田んぼ用に区画整理されていた"),
            asami.do("ここまで一時間程度は掛かっただろうか。もう充分に日が高く、私の首筋を幾筋も汗が流れ落ちて、下着がじっとりとしていた"),
            asami.talk("いた……"),
            asami.do("けれどここまで来たことは全然無駄じゃなかった。カーキ色の庇《ひさし》が付いたトラクターの上、見慣れたスポーツ刈りがランニングシャツ姿で乗り込んで操作している"),
            asami.talk("おーい"),
            asami.do("ずっと見つけたら何て言おうか考えていたのに、ここまで来るので疲れてそれどころじゃなくなってしまった。それで出た言葉はなんて平凡な呼びかけなのだろうと思ったけれど、"),
            tagawa.talk("なに？"),
            asami.do("案外うまくいったんじゃないかと、内心ではほっとした"),
            asami.talk("何？　じゃないです。何で田川君はこんなとこでトラクター動かしてるの？"),
            asami.do("ちゃんと聴こえたのだろうか、と不安になるくらい大きなエンジン音で、自転車を置いて近くまで畦を歩いて寄ってみたけれど、田川君は表情一つ変えずに何かの作業を続けていた"),
            asami.talk("ねーえー？"),
            tagawa.talk("わりぃ。これ終わるまで待ってくれ"),
            asami.talk("いいけどー"),
            asami.do("とは答えたものの、まだまだ田川君が作業している田んぼは草が生え放題の箇所ばかりだった"),
            asami.do("私は足を折り畳んでしゃがみ込み、頬に手を当ててしばらく彼が器用に大きな機械を動かすのを見守った。庇で陰になった田川君の表情は、普段学校で見せない充実した笑みを作っていて、何が面白いのか分からないけれど、何だかちょっとだけ羨ましい気持ちが生まれた"),
            w.br(),
            asami.do("結局彼が作業に一区切り付けてトラクターを下りてきたのは、お昼のサイレンが鳴り響いたすぐ後のことだった"),
            asami.talk("はいこれ"),
            asami.do("と、ひんやり汗をかいたサイダーの缶を彼に差し出す"),
            tagawa.talk("サンキューな"),
            asami.do("そう言って彼は受け取るなりプシュリと良い音をさせて開封し、喉《のど》がひりつくのも構わずに一気にそれを流し込む"),
            asami.do("だから思い切り噎《む》せて危うく中身を私にぶちまけそうになったが、寸でのところで何とか留まり、それからじっと互いを見やって、どちらともなく笑い出した"),
            asami.do("私も自分用に買ったオレンジジュースを開けて一口飲むと、それを見て彼は笑いながらこう言った"),
            tagawa.talk("俺もオレンジの方が良かった"),
            asami.talk("え？　そうなの？　ごめんなさい。けどもう飲んじゃったし"),
            tagawa.talk("いいよ。炭酸そこまで苦手って訳じゃないし"),
            asami.do("それでも田川君は何度か飲んでは苦しそうに噎せていた"),
            asami.talk("あのさ"),
            tagawa.talk("なんで浅見まで学校サボったの？"),
            asami.do("気になったから、とは言えなかった"),
            asami.talk("田川日和"),
            tagawa.talk("あぁ"),
            asami.do("彼はそうつまらなさそうに返すと、私を見て、それから目の前に広がる何枚もの田んぼへと視線を投げやった"),
            tagawa.talk("ここ全部さ、祖父さんの田んぼなんだよ"),
            asami.talk("それをなんで田川君が耕してるの？"),
            tagawa.talk("聞いてないんだな"),
            asami.do("サイダーを飲み干して缶を草むらに置くと、彼は立ち上がり、またトラクターに乗り込もうとする"),
            tagawa.talk("実はさ、祖父さんまた先週から入院してんだ。俺ががんばらないと田植えが終わらないんだわ"),
            asami.talk("え？"),
            asami.do("知らなかった。クラスの誰もそんなことは言っていなかったし、担任だって一言も教えてくれなかった"),
            tagawa.talk("なあ浅見"),
            asami.do("彼はトラクターの運転席に乗り込むと私を見てこんなことを尋ねた"),
            tagawa.talk("浅見には将来の夢ってあるのか？"),
            asami.do("将来も夢も、実は今一番耳にしたくない言葉だった"),
            )

def sc_rain(w: World):
    asami = w.get("asami")
    eri = w.get('eri')
    tagawa = w.get('tagawa')
    return w.scene("雨",
            asami.do("翌日は雨だった"),
            asami.do("土曜日は午前中だけで授業は終わりだったが、そこにはちゃんと田川君の姿もあり、普通に周りの男子と楽しそうに喋っていて、授業中に竹村から叱られていた"),
            asami.do("母方の祖父の実家に急遽作られた私の部屋は、畳敷きの和室で、腐っていたものを全て真新しくしたらしく、藺草《いぐさ》の香りが寝ている間も私を襲ってくる"),
            asami.do("ベッドのない生活になって、父親が戸籍から外れて、通学が電車から自転車に変わってしまって。それなのに私は何も変わらずにいる"),
            asami.do("夏頃にはもうどこの大学に行くのか決めないといけない。そんな風に前の学校では言われていたのに、担任の竹村からは、色々と家庭の事情もあるだろうから何だったら今回の調査票は白紙でも良い、なんて言われてしまった"),
            asami.do("寝転がる。天井を見上げても未来なんて見えないからと畳にキスしてみても、誰も答えを教えてくれない"),
            asami.do("それでも雨音を聞いている内に眠気がやってきて、私は午睡に落ちていった"),
            w.symbol("　　　　◆"),
            asami.do("週明けの月曜には先生から小テストをやると宣告されていた"),
            asami.do("にも関わらず、今日も田川日和だ。彼は教室にいない"),
            asami.talk("ねえ足立さん。田川君欠席だけど良いの？　学校卒業できなくなるんじゃないの？"),
            asami.do("私が転校してくるまでもかなり欠席していると聞いていた"),
            eri.talk("別に中退になっても良いってことじゃないの"),
            asami.talk("え？　だってそれじゃあ中卒だよ？"),
            eri.talk("あさみんはさ、どうしてそこまで田川のこと気にするの？　この前も訊いたけど、ほんとに好きじゃないんだよね？"),
            asami.do("これは恋愛感情、じゃない。その確信だけはあった。でも平気で学校を休んでトラクターを乗り回す田川君のことも、それに慣れ切った周囲の生徒たちのことも、気になってどうしようもなかった"),
            asami.talk("なんで誰も疑問じゃないの？"),
            eri.talk("急にどうしたのあさみん"),
            asami.do("体を半分｜捻《ひね》って後ろを向いていた足立さんはあまりに驚いたのか、背中を伸ばした拍子に捻ったらしく、低い唸《うな》り声を上げながら前を向いて机に突っ伏した"),
            asami.talk("大丈夫……？"),
            eri.talk("……人生で二番目に痛いよ"),
            asami.talk("ごめん……"),
            asami.do("そう謝ったものの、大きな声になった憤りは全然収まってなくて、結局その後に始まった古典の小テストでは、全然マスが埋められないまま試験時間が終わってしまった"),
            w.symbol("　　　　◆"),
            asami.do("試験が終わったその足で、私は田川君の田んぼに向かった"),
            asami.talk("やっぱり居た"),
            asami.do("彼は相変わらず一人でトラクターを動かして、まだ準備が済んでいない田んぼの土起こしをしている"),
            asami.talk("ねえ田川君？"),
            asami.do("なるべく大きな声で呼びかけてみたが聴こえていないのか、トラクターが止まることはない。それでも構わずに私は続ける"),
            asami.talk("なんで？　今日試験だって知ってたでしょ？　どうしてまたサボってこんなことしてるの？"),
            tagawa.talk("田川日和だろ？"),
            asami.talk("何でも田川日和って言えば許されるなんて思ってちゃ駄目だよ。自分の好き勝手してたらそのうちに愛想尽かされて捨てられちゃうかもなんだから！"),
            asami.do("彼はエンジンを止めると一度だけきつく睨むように見ると、"),
            tagawa.talk("たかが小テスト休んだくらいで誰も死なないだろ？　そもそも何で浅見は俺にそんな鬱陶《うっとう》しいんだよ"),
            asami.do("鬱陶しい。それは私の母親が元父親から言われた言葉だった"),
            asami.talk("わ、私は田川君の将来が心配だから言ってあげてるだけで、そんな風に言うならもういいよ"),
            asami.do("何だか背中の方が痛くなって、自転車の方に戻ろうとする"),
            tagawa.talk("浅見"),
            asami.do("振り返ると、彼がようやくトラクターを下りたところだった"),
            tagawa.talk("浅見にはさ、自分の日和はないのか？"),
            asami.talk("何よそれ"),
            tagawa.talk("俺には田川日和がある。お前にだって何か日和があるはずだろ。それが分かれば、小テストなんて大した問題じゃないって分かる"),
            asami.talk("そんなの分かる訳ないじゃん！　私には学校をサボったり小テストを休んだりするのに充分な理由なんて、どこにもないよ！"),
            tagawa.talk("そういうことじゃねえんだけど……"),
            asami.do("小さく首を振ると、田川君は再びトラクターに戻っていった。それからはいくら見つめてみても、彼は何一つ言葉を返してくれなくなった"),
            )

def sc_myfuture(w: World):
    asami = w.get("asami")
    return w.scene("進路",
            asami.do("結局白紙の進路調査票を提出して、元号が変わってしまったゴールデンウィークに突入した"),
            asami.do("当然私はどこに出かける予定もなく、クラスで唯一友だちのようなものになれた足立さんとも別に遊びに行くなんて話は出ず、ただ寝転がってＴＶの中で芸能人が楽しげに令和と話すのを見ているだけだ"),
            asami.do("ひょっとしたら私日和ってこういう退屈さの延長なのだろうか"),
            asami.do("だとしたら、私日和なんてずっとやって来なくて良い"),
            asami.talk("夕子ご飯"),
            asami.talk("はーい"),
            asami.do("滑り台のような急角度の階段を下りていくと、開け放たれた襖の間から既に食卓に集まっている家族の姿が見えた"),
            asami.do("じいちゃんとばあちゃん、それにお母さんと弟の正嗣《まさし》。変わらない家族の顔。弟は来年高校生だが私よりも頭二つ分ほどでかい。バスケができればどこでも良いという飄々とした性格が、私は少し羨ましかった"),
            asami.talk("いただきます……"),
            asami.do("ご飯が山盛りにされている"),
            asami.do("祖父の家に来て一番変わったことは、ご飯と野菜が大量に食卓に並ぶようになったことだ"),
            asami.do("じいちゃんはまだ現役で稲作農家だし、家の裏側には広大な畑が年中通して何かしら植えられている。何か欲しければスーパーに、ではなく、畑に行って収穫をすればいい"),
            asami.do("そんな暮らしが母は少しだけ楽しそうだ"),
            asami.do("ただそれでも、知らない間に髪に白いものは増えたし、何よりあんなに毎朝きっちりと整えていた髪が、今日はどこにも出かけないからか、ボサボサのものをヘアピンで右側に束ねていた"),
            asami.talk("そういえば夕子、お前田川んちの坊主と付き合ってるってほんとか？"),
            asami.do("その祖父の言葉に私は思わず口に入れたほうれん草の胡麻和《ごまあ》えを吐き出すところだった"),
            asami.talk("な、何なのよそれ。誰がそんなこと言ってたの？"),
            asami.talk("誰って……"),
            asami.do("そう口籠るとじいちゃんは目線をばあちゃんの方に移す。その目線をばあちゃんが今度はお母さんに移し、最後にはお母さんが私を見た"),
            asami.talk("何なのよ"),
            asami.talk("夕子が田んぼでデートしてたってみんな言ってたわよ？"),
            asami.talk("違うわよ。あれは田川君が学校サボってたから注意しに行っただけ。別に恋とかそんなんじゃないし"),
            asami.talk("そういうの世話焼き女房って言うらしい"),
            asami.do("ぼそっと低音で弟がそんなことを言う。私は咄嗟《とっさ》に睨《にら》みつけたが平気な顔をして正嗣はご飯のお替りをした"),
            asami.talk("だって田川君さ、学校やテストなんて別にどうだっていいって言うんだよ？　天気が良いからサボりましたとか、そんなの社会に出たら通用しないよ"),
            asami.talk("それならワシも通用してないんやろうね"),
            asami.talk("え？"),
            asami.talk("よく田川と二人で学校抜け出しては山に入って駆け回ってたからな。ワシらが小さかった頃は食べるもんが畑か山か川だった。けど畑のもん勝手に取ったら祖父さんらにゲンコツされるし、結局山ん中がワシらの戦場だったな"),
            asami.do("じいさん。そう言ってばあちゃんはほっぺを抓《つね》ると、私に向かって笑い掛けた"),
            asami.talk("学校に行くことも大事。でも田んぼの準備は今しかできんからねえ。ほら、田川さんとこまた入院されてるでしょ。息子さんが手伝ってくれるようになって随分《ずいぶん》助かってるって言ってたわよ。それが悪いこととはわたしには言えないわ"),
            asami.talk("けど"),
            asami.talk("しなきゃならないことばかりだと、相手が疲れちゃうのかもね。ねえ夕子、あなたのしたいことって何なんだろうね"),
            asami.do("少しだけ寂しそうに笑ってお母さんは私を見た"),
            asami.do("私のしたいこと"),
            asami.do("結局それがいつまで経っても見つけられない"),
            )

def sc_ending(w: World):
    asami = w.get("asami")
    tagawa = w.get('tagawa')
    return w.scene("休日終わり",
            w.symbol("　　　　◆"),
            asami.do("長かったゴールデンウィークも明日で終わる"),
            asami.do("私はばあちゃんから教えてもらった田川君の実家に一人でやってきた。当然何の連絡もしていない"),
            asami.do("驚くほどの晴天で、実に田川日和だ。彼がいない可能性の方がずっと高かった"),
            asami.do("それでも、とインタフォンらしきボタンを押す。ジィィ、と油蝉《アブラゼミ》の鳴き声みたいな音がして、しばらくすると田川君が顔を出した"),
            tagawa.talk("何？"),
            asami.talk("なんで田んぼに出てないのよ"),
            tagawa.talk("今日はこれから祖父さんの見舞い"),
            asami.talk("あ、ごめん……"),
            asami.do("田川君は別にいいよ、と呟いてから「で？」と私を訝《いぶか》しげに見た"),
            asami.talk("この前のこと"),
            tagawa.talk("この前？"),
            asami.talk("自分日和"),
            tagawa.talk("ああ。なんか妙なこと言って悪かった。その、浅見も色々あるんだよな"),
            asami.talk("そうじゃない。そんなことじゃないの"),
            tagawa.talk("そんなことってな。俺なんかうちの両親が離婚したらものすっごく困るぞ"),
            asami.do("田川君が突然あまりにも真面目な顔をして言うものだから、私は何だかおかしくなって吹き出してしまう"),
            tagawa.talk("んだよ"),
            asami.talk("あのさ、田川君って付き合っている人とか、いるの？"),
            tagawa.talk("はあ？　なんだよそれ"),
            asami.talk("いいから。いるいない、どっち？"),
            tagawa.talk("い、いねえよ"),
            asami.talk("それじゃあ十年後って何してる？"),
            asami.do("またかよ。そんな顔をして私を見たが、じっと考え込むと田川君は小さく溜息を零《こぼ》してから、こう答えてくれた"),
            tagawa.talk("農家。俺はずっと小さい頃から祖父さんみたいな米や野菜作りがしたいんだよ"),
            asami.talk("うん。やっぱりそうだよね"),
            asami.do("彼は相変わらず分からないといった表情だが、私には充分な答えだった"),
            asami.talk("これ"),
            asami.do("と彼に見せたのは、先生が余分にくれた進路調査票だった。そこには『幸せな家庭』と書かれている"),
            tagawa.talk("これが浅見日和か？"),
            asami.talk("馬鹿にしないの？"),
            tagawa.talk("俺には良い日和に見えるけどな"),
            asami.do("そう言って田川君は親指を立てて見せると、"),
            tagawa.talk("ちょっと待ってろ"),
            asami.do("何故か突然家の中に引っ込んでしまう"),
            asami.talk("何なのよ……"),
            asami.do("ニ、三分だろうか、玄関で待ち呆けていると戻ってきた田川君の手には彼の足のような立派な太さの大根が握られていた。ただ長さが売り場に出ているものの半分程度だ"),
            asami.talk("何？"),
            tagawa.talk("田川日和"),
            asami.talk("え？"),
            tagawa.talk("俺が今年植えた春大根だよ。もうこんなになったんだけど、まだ売り場には出せないってさ"),
            asami.do("見れば分かる。けど出来損ないかも知れなくても私にはそれがとても美味しそうに思えた"),
            tagawa.talk("あと十年もすればもっと立派なのじゃんじゃん作れるようになるさ。そん時までには上手く大根炊けるようになっといてくれると助かる"),
            asami.do("彼は私を見て照れ臭そうにそう笑ったが、"),
            asami.talk("ねえ。なんで私が料理下手なの知ってるの？"),
            tagawa.talk("えっと……うちの祖父さんが"),
            asami.talk("あぁ……もうこれだから田舎は！"),
            asami.do("思い切り拳を握り締めた私を見て、田川君は大きな声で笑った"),
            asami.do("その笑顔はまるで太陽そのもので、これが本当の田川日和なんだと、クラスのみんなが彼を愛する気持ちが今更に理解できた気がした"),
            asami.do("十年後どころか五年後だって自分がどうなっているかなんて分からない。けど、今見つけた自分日和を大切にした先にこんな風に笑える未来があるのかな、なんて思えるようになっただけ、平成に置き去りにされた自分からは成長できたのかも知れなかった"),
            )

