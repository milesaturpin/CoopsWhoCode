var elements = document.getElementsByTagName('*');

var replacements = {};
replacements["oo"] = "∞";
replacements["Luke Farrell"] = " trash ";
replacements["Eric Ramoutar"] = "Barack Ramoutar";
replacements["Lardaro"] = "the Snake";
replacements["absolutely"] = "aaaaaaaaabbbbsssolutely";
replacements["About"] = " Lemme tell ya about ";
replacements["Mirecourt"] = "";
replacements["strong"] = "big boy";

/*
ADD YOUR OWN
pretty self explanitory but you can copy-paste this line
replacements[""] = "";
and fill in the blanks. 
Then, just put it beneath the examples higher on the page
*/

for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        if (node.nodeType === 3) {
            var text = node.nodeValue;
            for(key in replacements){
                if(text.includes(key)){
                    var rt = text.replace(key,replacements[key]);
                    if (rt !== text) {
                        element.replaceChild(document.createTextNode(rt), node);
                    }
                }
            }
        }
    }
}