function solution(t, p) {
    var answer = 0;
    var t_num = 0;
    var p_num = parseInt(p)
    var end = p.length
    
    for (var i = 0; i < t.length - p.length + 1; i++){
        t_num = parseInt(t.slice(i,end))
        if(t_num <= p_num){
            answer += 1 
        }
        end += 1
    }
    
    return answer;
}