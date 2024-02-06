class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        updated_points = []
        for item in points:
            if item not in updated_points:
                updated_points.append(item)
        if len(updated_points) < 3:
            return len(updated_points)
        def add_dict(a_dict, a_slope, a_interception, a_point):
            the_key = 'slope:'+str(a_slope)+' interception:'+str(a_interception)
            if the_key in a_dict:
                if a_point not in a_dict[the_key][0]:
                    a_dict[the_key][0].append(a_point)
                    a_dict[the_key][1] += 1
            else: 
                a_dict[the_key] = [[a_point],1]

            return a_dict

        # def find_mode(a_list):
        #     a_dict = {}
        #     for item in a_list:
        #         if item in a_dict:
        #             a_dict[item] += 1
        #         else:
        #             a_dict[item] == 1
        #     result = 0
        #     for key, value in a_dict:
        #         if value > result:
        #             result = value
        #     return result

        # find most common slope
        # find most common interception: b
        # y = ax +b
        # if line is vertical, slope is None.
        # if line is horizontal, slope is 0.
        slope_dict = {}


        current_index = 0
        while current_index < len(updated_points)-1:
            current_point = updated_points[current_index]
            compare_current_point = current_index + 1
            for i in range(compare_current_point, len(updated_points)):
                if updated_points[i][0]-current_point[0] != 0:
                    current_slope = (updated_points[i][1]-current_point[1])/(updated_points[i][0]-current_point[0])
                    interception = updated_points[i][1] - current_slope*updated_points[i][0]
                    slope_dict = add_dict(slope_dict, current_slope, interception, updated_points[i])
                    slope_dict = add_dict(slope_dict, current_slope, interception, current_point)
                else:
                    slope_dict = add_dict(slope_dict, 'infi', current_point[0], updated_points[i])
                    slope_dict = add_dict(slope_dict, 'infi', current_point[0], current_point)      
            current_index += 1

        result = 0
        for k, v in slope_dict.items():
            if v[1] > result:
                result = v[1]
        return result

