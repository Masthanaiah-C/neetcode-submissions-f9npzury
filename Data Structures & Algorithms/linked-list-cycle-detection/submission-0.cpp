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
    bool hasCycle(ListNode* head) {
        //Base Condition
        if (head == NULL || head->next == NULL) {
            return false;
        }

        //Atleast 2 nodes are there
        ListNode* curNode = head;
        ListNode* fastNode = head->next;
        int counter = 0;

        while (fastNode->next != NULL && fastNode->next->next !=NULL) {
            if (curNode == fastNode) {
                return true;
            }
            curNode = curNode->next;
            fastNode = fastNode->next->next;
        }

        return false;
    }
};
