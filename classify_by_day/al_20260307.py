from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ### First Approach (Too slow)
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        elif len(inorder) == 0:
            return None

        root = postorder[-1]

        left_in, right_in = {}, []
        left_post, right_post = [], []
        flag = True
        for i in range(len(inorder)):
            n = inorder[i]
            if n == root:
                flag = False
                continue
            if flag:
                left_in[n] = True
            else:
                right_in.append(n)

        for n in postorder[:-1]:
            if n in left_in:
                left_post.append(n)
            else:
                right_post.append(n)

        left = self.buildTree(list(left_in.keys()), left_post)
        right = self.buildTree(right_in, right_post)

        return TreeNode(root, left, right)

        ### Second Approach
        # hashmap = {n: index for index, n in enumerate(inorder)}
        # self.root = len(inorder)-1
        # def create_build_tree(left_idx, right_idx):
        #     if left_idx > right_idx:
        #         return None
        #     root = TreeNode(postorder[self.root])
        #     self.root -= 1
        #
        #     mid_idx = hashmap[root.val]
        #
        #     root.right = create_build_tree(mid_idx+1, right_idx)
        #     root.left = create_build_tree(left_idx, mid_idx-1)
        #
        #     return root
        #
        # return create_build_tree(0, self.root)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.buildTree([9,3,15,20,7], [9,15,7,20,3]))
    print(sol.buildTree([2, 1], [2, 1]))

explain = """In inorder traversal, elements on the left side of the root index belong to the left subtree, 
and elements on the right side belong to the right subtree.
If we iterate backward through postorder traversal, we encounter nodes in the order:
root -> right subtree -> left subtree.
Using this property, we can recursively construct the binary tree.  
"""