package com.bitcamp.baekjoon;

public class Pg210815 {
	class Solution {
	    public int solution(int[][] board, int[] moves) {
	        int answer = 0;
	        int[] basket = new int[1000];
	        int pointer = 0; // basket 포인터
	        for(int a : moves){
	            for(int i=0; i<board.length; i++){
	                if(board[i][a-1] != 0){
	                    System.out.println("들어옴"+board[i][a-1]);
	                    basket[pointer] = board[i][a-1]; // 포인터가 위치한 자리에 배열 인형 넣기
	                    board[i][a-1] = 0;//인형 뺌
	                    if(pointer != 0 && basket[pointer] == basket[pointer-1]){ // 똑같은 번호가 들어오면
	                        basket[pointer] = 0;
	                        basket[pointer-1] = 0; // 초기화시켜주기
	                        answer = answer+2; // answer 더해주기
	                        pointer = pointer -2;
	                    }
	                    pointer++; //포인터 위치 더해주기
	                    break;
	                }
	            }
	        }
	        return answer;
	    }
	}
}
