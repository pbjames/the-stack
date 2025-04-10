export interface Todo {
  id?: number;
  creation_timestamp: number;
  completion_timestamp: number;
  content: string;
  user_id: number;
}

export interface User {
  id?: number;
  username: string;
  password: string;
  email: string;
}
