// in src/users.js
import React, {FC} from 'react';
import {
    List,
    Datagrid,
    TextField,
    BooleanField,
    EmailField,
    EditButton,
} from 'react-admin';

export const UserList: FC = (props) => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id"/>
            <EmailField source="email"/>
            <TextField source="first_name"/>
            <TextField source="last_name"/>
            <BooleanField source="is_superuser"/>
            <EditButton/>
        </Datagrid>
    </List>
);

export const AuthorList: FC = (props) => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id"/>
            <TextField source="full_name"/>
            <EditButton/>
        </Datagrid>
    </List>
);

export const BookList: FC = (props) => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id"/>
            <TextField source="title"/>
            <TextField source="description"/>
            <TextField source="image_url"/>
            <TextField source="author_id"/>
            <TextField source="review_hour_amount"/>
            <EditButton/>
        </Datagrid>
    </List>
);

export const ReviewList: FC = (props) => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id"/>
            <TextField source="text"/>
            <TextField source="user_created_id"/>
            <TextField source="book_id"/>
            <TextField source="created_at"/>
            <EditButton/>
        </Datagrid>
    </List>
);