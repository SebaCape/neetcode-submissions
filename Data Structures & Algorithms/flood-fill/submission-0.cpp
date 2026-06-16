class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) 
    {
        //Track initial color, initialize queue with starting value, and track image size
        int init_color = image[sr][sc];

        queue<tuple<int, int>> q;
        q.push({sr, sc});

        int R = image.size(), C = image[0].size();


        while(!q.empty())
        {
            //Unpack our tuple
            auto[row, col] = q.front();
            q.pop();

            //Skip invalid values
            if(row >= R || col >= C || row < 0 || col < 0 || image[row][col] == color)
                continue;

            //Create deque of valid adjacent values
            deque<tuple<int, int>> d = {
                {row + 1, col},
                {row, col + 1},
                {row - 1, col},
                {row, col - 1}
            };

            //Set color if valid and add adjacent coordinates
            if(image[row][col] == init_color)
            {
                image[row][col] = color;
                while(!d.empty())
                {
                    //Grab valid coordinates from tuple and add to our queue
                    tuple<int, int> nc = d.front();
                    d.pop_front();

                    if(get<0>(nc) >= R || get<1>(nc) >= C || get<0>(nc) < 0 || get<1>(nc) < 0)
                        continue;
                    else
                        q.push(nc);
                }
            }
        }

        return image;
    }
};