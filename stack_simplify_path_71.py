class Solution:
    def simplifyPath(self, path: str) -> str:
        # others:
        components = path.split('/')
        stack = []

        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component and component != '.':
                stack.append(component)

        simplified_path = '/' + '/'.join(stack)
        return simplified_path  





        # # my solution:
        # # check first /
        # # check last /
        # # check consecutive //
        # # record level up
        # # record level down
        # if len(path) == 1 and path[0]=='/':
        #     return path
        # if path[0] != '/':
        #     path = '/'+path
        # if path[-1] == '/':
        #     path=path[:-1]
        # # print(path)

        # last = None
        # current = ''
        # for item in path:
        #     if item == '/' and last == '/':
        #         continue
        #     else:
        #         current += item
        #         last = item
        # if current[-1] == '/':
        #     current=current[:-1]
        # path_list = current.split('/')
        # level_up = 0
        # level_down = 0
        # path_list_len = len(path_list)
        # result_path_list = []

        # for i in range(1, path_list_len):
        #     if path_list[i] == '..':
        #         level_up += 1
        #         result_path_list = result_path_list[:-1]

        #     elif path_list[i] == '.' or path_list[i] == '':
        #         continue
        #     else:
        #         level_down += 1
        #         result_path_list.append(path_list[i])
        #     # print(f'leve_up: {level_up}')
        #     # print(f'level_down: {level_down}')

        #     print(f'result_path_list: {result_path_list}')    

        # # if level_up > level_down:
        # #     return '/'
        # # if level_up == level_down:
        # #     return '/'

        # # down_level = level_down - level_up
        # # result_list = [] 
        # # # print(f'path_list: {path_list}')
        # # for i in range(1, path_list_len):
        # #     if path_list[i] != '..' and path_list[i] != '.':
        # #         result_list.append(path_list[i])
        # #         down_level -= 1
        # #         if down_level == 0:
        # #             break
        # # # print(f'result_list: {result_list}')
        # print(f'result_path_list: {result_path_list}')
        # if len(result_path_list) == 1:
        #     result_str = '/'+result_path_list[0]
        # else:
        #     result_str = '/'.join(result_path_list)
        #     result_str = '/'+result_str
        # # print(result_list)
        # return result_str
