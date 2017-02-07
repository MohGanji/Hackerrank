// The problem is here:
// https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

#include <iostream>
#include <stack>
using namespace std;

#define Stack1 stack_newest_on_top
#define Stack2 stack_oldest_on_top

class MyQueue {

public:
	stack<int> stack_newest_on_top, stack_oldest_on_top;   

	void replace(){
		while(!Stack1.empty()){
			Stack2.push(Stack1.top());
			Stack1.pop();
		}
	}

	void push(int x) {
		Stack1.push(x);
	}

	void pop() {
		if(Stack2.empty())
			replace();
		Stack2.pop();
	}

	int front() {
		if(Stack2.empty())
			replace();
		return Stack2.top();
	}
};

int main() {
	MyQueue q1;
	int q, type, x;
	cin >> q;

	for(int i = 0; i < q; i++) {
		cin >> type;
		if(type == 1) {
			cin >> x;
			q1.push(x);
		}
		else if(type == 2) {
			q1.pop();
		}
		else cout << q1.front() << endl;
	}

	return 0;
}

