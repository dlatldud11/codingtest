package com.bitcamp.baekjoon;

public class Class {
	class Solution {
	    public int[] solution(int[] fees, String[] records) {
	        int[] answer = {};
	        int[][] arr = new int[10000][4]; // 번호판과 인아웃시간 금액 누적시간
	        int pay = 0; //가격
	        for(int i=0; i<records.length; i++){
	            String[] str = records[i].split(" "); //시간 번호판 인아웃
	            if(str[2].equals("IN")){ //들어올때면
	                String[] time = str[0].split(":"); // 시: 분 나눔
	                int hap = Integer.parseInt(time[0])*60 + Integer.parseInt(time[1]);
	                arr[Integer.parseInt(str[1])][0] = hap; //들어오는 시간
	                System.out.println(hap+"IN"+str[1]);
	            }
	            else if(str[2].equals("OUT")){ // 나갈때면
	                String[] time = str[0].split(":"); // 시: 분 나눔
	                int hap = Integer.parseInt(time[0])*60 + Integer.parseInt(time[1]);
	                arr[Integer.parseInt(str[1])][1] = hap; // 나가는 시간
	                System.out.println(hap+"OUT"+str[1]);
	                arr[Integer.parseInt(str[1])][3] = arr[Integer.parseInt(str[1])][1] - arr[Integer.parseInt(str[1])][0]; // 누적 시간 넣어놓기
	                arr[Integer.parseInt(str[1])][0] = 0;
	                arr[Integer.parseInt(str[1])][1] = 0; //inout 초기화
	                
	        }
	        }
	        for(int i=0; i<arr.length; i++){ // 번호판 개수
	            if(arr[i][0] != 0){ // 인만 있으면
	                       double plus = (arr[i][3] +1439 - arr[i][0] - fees[0])/fees[2];
	                       pay = fees[1] + ((int)Math.ceil(plus) * fees[3]);
	                   }
	            else{ // 누적 시간만 있으면
	                 double plus = (arr[i][3] - fees[0])/fees[2];
	                       pay = fees[1] + ((int)Math.ceil(plus) * fees[3]);
	            }
	                 arr[i][2] = pay;
	                System.out.println(arr[i][2] +"out없을때"+i+"pay"+pay);
	            
	            if(arr[i][1] != 0){
	                System.out.println(i+"/"+arr[i][2]);
	            }
	    }
	        return answer;

	}
	    
	}
}
