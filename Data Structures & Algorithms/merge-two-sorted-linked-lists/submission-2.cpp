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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Base Conditions
        if (list1 == NULL) {
            return list2;
        }
        else if (list2 == NULL) {
            return list1;
        }

        // Both heads are non-empty. Merge to List 1
        ListNode* curlist1;
        ListNode* curlist2;
        
            curlist1 = list1;
            curlist2 = list2;
            
        
        ListNode* final = NULL;
        ListNode* gFinal = NULL;
        while(curlist2 != NULL or curlist1 != NULL) {
            if( curlist2 == NULL) {
                final->next = curlist1;
                return gFinal;
            } 
            if (curlist1 == NULL){
                final->next = curlist2;
                return gFinal;
            }
            if(curlist2->val >= curlist1-> val) {
                if (final == NULL) {
                    final = curlist1;
                    gFinal = final;
                    curlist1= curlist1->next;
                    continue;
                }
                ListNode* nextcurlist1 = curlist1->next;
                ListNode* nextfinal = final->next;
                final->next = curlist1;

                curlist1->next = nextfinal;

                final = final->next;
                curlist1 = nextcurlist1;
            } else {
                if (final == NULL) {
                    final = curlist2;
                    gFinal = final;
                    curlist2= curlist2->next;
                    continue;
                }
                ListNode* nextcurlist2 = curlist2->next;
                ListNode* nextfinal = final->next;
                final->next = curlist2;

                curlist2->next = nextfinal;

                final = final->next;
                curlist2 = nextcurlist2;
            }
        }
        return final;
        
    }
};
