package com.bitcamp.isy;

import java.util.ArrayList;
import java.util.List;

public class Student {
	String name;
	String email;
	String phonenumber;
	String id;
	public Student() {
		name = null;
		email = null;
		phonenumber = null;
		
	}
	

	@Override
	public String toString() {
		
		return " "+id+"\t"+name+"\t"+email+"\t"+phonenumber;
	}
			 


	public String getId() {
		return id;
	}


	public void setId(String id) {
		this.id = id;
	}


	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPhonenumber() {
		return phonenumber;
	}
	public void setPhonenumber(String phonenumber) {
		this.phonenumber = phonenumber;
	}


	
}
