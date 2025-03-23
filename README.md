# danbooru tag classification
[Perplexity](https://www.perplexity.ai/)のClaude3.7 Sonnetのプロサーチでdanbooruのgeneral tagを分類しました。  
分類先のカテゴリは[prompt.md](./prompt.md)を参照してください。  
カテゴリごとのワイルドカードも用意しています。

## 分類対象のタグ
[general.csv](./general.csv)  
[2024-11-9時点のdanbooruタグ](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete/blob/6ffeeafc49256106266922989ffe8b6b5ef4981f/tags/danbooru.csv)のうち、type=0(general)のタグ

## プロンプト
### 初回
[prompt.md](./prompt.md)  

### 2回目以降
分類するタグのみを返信する。  
例 :   
```
cum_in_pussy
halterneck
beret
...
neck_bell
colored_sclera
gold_trim
```
