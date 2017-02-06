// The problem is here:
// https://www.hackerrank.com/challenges/ctci-balanced-brackets

#include <stack>
#include <iostream>


using namespace std;


bool is_balanced(string str) {
	stack<char> s;
	int ind = 0;

	while(ind < str.length()){
		if( str[ind] == '[' or str[ind] == '(' or str[ind] == '{')
			s.push(str[ind]);
		else if(s.empty())
			return false;
		else if(int(str[ind] - s.top()) == 1 or int(str[ind] - s.top()) == 2)
			s.pop();
		else
			return false;
		ind++;
	}
	return s.empty();
}

int main(){
	cerr << int(']'-'[') << endl;
	cerr << int('}'-'{') << endl;
	cerr << int(')'-'(') << endl;
	int testcases;
	cin >> testcases;
	for(int i = 0; i < testcases; i++){
		string expression;
		cin >> expression;
		string answer = is_balanced(expression) ? "YES" : "NO";
		cout << answer << endl;
	}
	return 0;
}

