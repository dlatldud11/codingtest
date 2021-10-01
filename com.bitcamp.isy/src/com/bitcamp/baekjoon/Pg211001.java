package com.bitcamp.baekjoon;

public class Pg211001 {
	class Solution {
	    public int solution(int n, int[] lost, int[] reserve) {
	        int answer = 0;
	        int[] d = new int[n];
	        for(int i=0; i<n; i++){
	            d[i] = 1;
	        }
	        for(int i=0; i<lost.length;i++){
	            d[lost[i]-1] -= 1; // 체육복 잃어버림
	        }
	        for(int i=0; i<reserve.length; i++){
	            d[reserve[i]-1] += 1; // 체육복 여분 있음
	        }
	        for(int i=0; i<d.length; i++){
	            if(i == 0 && d[i] == 0){
	                if(d[i+1] == 2){
	                    d[i] ++;
	                    d[i+1] --;
	                }
	            }else if(i == d.length-1 && d[i] == 0){
	                if(d[i-1] == 2){
	                    d[i]++;
	                    d[i-1]--;
	                }
	            }else if(d[i] == 0){
	                if(d[i-1] == 2){
	                    d[i] ++;
	                    d[i-1] --;
	                }else if(d[i+1] == 2){
	                    d[i] ++;
	                    d[i+1] --;
	                }
	            }
	        }
	        for(int i=0; i<d.length;i++){
	                if(d[i] > 0){
	                    answer++;
	                }
	            }
	        return answer;
	    }
	}

}
