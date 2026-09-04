import java.util.*;

class Page {
    int link, base_score;
    double match_score;
    int index;
    ArrayList<Integer> links;
    public Page(){
        links = new ArrayList<>();
    }
    
    public double getLinkScore() {
        if (links.isEmpty()) return 0;
        return (double) base_score / links.size();
    }
}

class Solution {
    HashMap<Integer, Integer> mapper;
    
    public int solution(String word, String[] pages) {
        int L = pages.length;
        Page[] arr = new Page[L];
        mapper = new HashMap<>();
        
        for (int i=0; i<L; i++){
            arr[i] = parseDOM(pages[i], word, i);
            arr[i].match_score += arr[i].base_score;
        }
               
        for (Page p : arr){
            for (int connected: p.links){
                Integer index = mapper.get(connected);
                if (index != null) {
                    arr[index].match_score += p.getLinkScore();
                }
                
            }
        }
        
        int answer = 0;

        for (int i = 1; i < L; i++) {
            if (arr[i].match_score > arr[answer].match_score) {
                answer = i;
            }
        }

    return answer;

    }
    
    //page와 소문자로 이루어진 word
    private Page parseDOM(String page, String target, int idx){
        ArrayList<String> words = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        Page ret = new Page();
        ret.index = idx;
        
        String[] myLink = getLink(page, "meta", "content");
        String[] links = getLink(page, "a", "href");
        
        ret.link = myLink[0].hashCode();
        mapper.put(ret.link, idx);
        
        for (String link : links){
            ret.links.add(link.hashCode());
        }
        
        for (char c: page.toCharArray()){
            if (Character.isAlphabetic(c)) sb.append(c);
            else {
                if (sb.length() == 0) continue;
                words.add(sb.toString());
                sb.setLength(0);
            }
        }
        
        for (String word : words){
            if (target.equalsIgnoreCase(word)) {
                ret.base_score++;
            }
        }
        
        return ret;
    }
    
    private String[] getLink(String page, String tag, String property){
        int tagStart = page.indexOf("<"+tag);
        ArrayList<String> ret = new ArrayList<>();
        
        while (tagStart != -1) {
            int tagEnd = page.indexOf(">", tagStart);

            if (tagEnd == -1) break;

            String sub = page.substring(tagStart, tagEnd + 1);

            int contentStart = sub.indexOf(property+"=\"");

            if (contentStart != -1) {
                contentStart += (property+"=\"").length();

                int contentEnd = sub.indexOf("\"", contentStart);

                if (contentEnd != -1) {
                        ret.add(sub.substring(contentStart, contentEnd));
                }
            }

            tagStart = page.indexOf("<"+tag, tagEnd + 1);
        }
        
        return ret.toArray(new String[0]);
    }
}