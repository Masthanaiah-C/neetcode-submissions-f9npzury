/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    int lengthLinkedList(ListNode* l) {
        if (l == NULL) {
            return 0;
        }
        int count = 0;
        while (l != NULL) {
            count++;
            l = l ->next;
        }
        return count;
    }
    ListNode* reverseLinkedList(ListNode* l) {
        // Base Condition 
        if (l == NULL || l->next == NULL) {
            return l;
        }

        // 3 Pointers - Previous, Cur, Next
        // 2. Fix: Use pointers for all variables
        ListNode* prev = l; 
        ListNode* cur = l;
        ListNode* nextNode = l->next;

        // First Node
        prev -> next = NULL;
        cur = nextNode;
        nextNode = cur->next;

        //Intermediate Nodes
        while(nextNode != NULL) {
            cur ->next = prev;
            prev = cur;
            cur = nextNode;
            nextNode = nextNode -> next;
        }

        // Last Node
        cur -> next = prev;
        return cur;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Idea: Reverse the LinkedList l1 and l2 and add them to l1 return reverse of l1
        // l1 = reverseLinkedList(l1);
        // l2 = reverseLinkedList(l2);
        int carry_enabled = 0;

        int carry = 0;
        // Assign l1 to the largest linkedlist
        if (lengthLinkedList(l2) > lengthLinkedList(l1)){
            ListNode* temp = l2;
            l2 = l1;
            l1 = temp;
        }
        ListNode* sum = l1;
        // Add 2 linked list Node by Node until one of them ends. 
        while ((l1 != NULL) &&( l2 != NULL)) {
            int sumNode = l1->val + l2->val + carry;
            carry = sumNode / 10 ;
            if (carry == 1) {
                carry_enabled = 1;
            }
            l1 ->val = sumNode%10;
            l1 = l1->next;
            l2 = l2->next;
        }

        

        // L2 ends
        while (carry && (l1 !=NULL)) {
            int sumNode = l1->val + carry;
            carry = sumNode / 10 ;
            l1 ->val = sumNode%10;
            l1 = l1->next;
        }

        // Both Ends. 
        if (carry) {
            sum = reverseLinkedList(sum);
            sum =  new ListNode(1, sum);
            sum = reverseLinkedList(sum);
        }
        
        
         
        return sum;



    }
};
