class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        cal_list = []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                cal_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        cal_list.sort()
        result = cal_list[1]-cal_list[0]
        if len(cal_list)>2:
            for i in range(1, len(cal_list)-1):
                current = cal_list[i+1]-cal_list[i]
                if current < result:
                    result = current
        return result
    
    