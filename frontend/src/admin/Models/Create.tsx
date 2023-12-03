import React, {FC} from 'react';
import {
    Create,
    SimpleForm,
    TextInput,
    PasswordInput,
    BooleanInput, TextField,
} from 'react-admin';

export const UserCreate: FC = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="email"/>
            <TextInput source="first_name"/>
            <TextInput source="last_name"/>
            <PasswordInput source="password"/>
            <BooleanInput source="is_superuser"/>
        </SimpleForm>
    </Create>
);

export const AuthorCreate: FC = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="full_name"/>
        </SimpleForm>
    </Create>
);

export const BookCreate: FC = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="title"/>
            <TextInput source="description"/>
            <TextInput source="review_hour_amount"/>
            <TextInput source="image_url"/>
            <TextInput source="author_id"/>
        </SimpleForm>
    </Create>
);

export const ReviewCreate: FC = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="text"/>
            <TextInput source="user_created_id"/>
            <TextInput source="book_id"/>
        </SimpleForm>
    </Create>
);