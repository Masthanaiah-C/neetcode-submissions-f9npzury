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
    void reorderList(ListNode* head) {
        // Base Conditions
        if (head == nullptr || head->next == nullptr) return;



        // Find middle Node
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow -> next;
            fast = fast -> next -> next;
        }
        
        // Save Slow 
        ListNode* saveSlow = slow;

        // Reverse the linklist from slow 
        ListNode* temp = slow -> next;
        ListNode* prev = slow;

        while(temp != nullptr) {
            ListNode* savetempnext = temp->next;
            if (prev == slow) temp ->next = nullptr;
            else temp -> next = prev;
            prev = temp;
            temp = savetempnext;
        }
        slow -> next = prev;

        temp = prev;
        slow -> next = nullptr;

        //Insertion logic 
        while (temp != nullptr) {
            ListNode* savenexthead = head -> next;
            ListNode* savenexttemp = temp -> next;
            head -> next = temp;
            temp -> next = savenexthead;
            head = savenexthead;
            temp = savenexttemp;
        }
        

        return ;
    }
};
