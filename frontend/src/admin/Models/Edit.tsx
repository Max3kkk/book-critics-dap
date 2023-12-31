import React, {FC} from 'react';
import {
    Edit,
    SimpleForm,
    TextInput,
    PasswordInput,
    BooleanInput,
} from 'react-admin';

export const UserEdit: FC = (props) => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput disabled source="id"/>
            <TextInput source="email"/>
            <TextInput source="first_name"/>
            <TextInput source="last_name"/>
            <PasswordInput source="password"/>
            <BooleanInput source="is_superuser"/>
        </SimpleForm>
    </Edit>
);

export const AuthorEdit: FC = (props) => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput disabled source="id"/>
            <TextInput source="full_name"/>
        </SimpleForm>
    </Edit>
);

export const BookEdit: FC = (props) => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput disabled source="id"/>
            <TextInput source="title"/>
            <TextInput source="description"/>
            <TextInput source="image_url"/>
            <TextInput source="review_hour_amount"/>
            <TextInput source="author_id"/>
            <TextInput disabled source="created_at"/>
        </SimpleForm>
    </Edit>
);

export const ReviewEdit: FC = (props) => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput disabled source="id"/>
            <TextInput source="text"/>
            <TextInput source="user_created_id"/>
            <TextInput source="book_id"/>
            <TextInput disabled source="created_at"/>
        </SimpleForm>
    </Edit>
);