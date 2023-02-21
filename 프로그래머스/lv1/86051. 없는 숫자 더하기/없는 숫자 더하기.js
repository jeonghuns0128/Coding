function solution(numbers) {
    var answer = -1;
    var total = 45;
    var sum = 0
    
    if(numbers.length > 0){
        for(var i of numbers){
            sum += i    
        }
        answer = total - sum
    }
    
    return answer;
}