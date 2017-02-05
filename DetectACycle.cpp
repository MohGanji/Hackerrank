// The problem is here:
// https://www.hackerrank.com/challenges/ctci-linked-list-cycle

bool has_cycle(Node* head) {
	int counter = 0;
	while( head != NULL){
		if (counter++ == 100)
			return true;
		head = head->next;
	}
	return false;
}

