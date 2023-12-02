import React from 'react';
import { fetchUtils, Admin as ReactAdmin, Resource } from 'react-admin';
import simpleRestProvider from 'ra-data-simple-rest';
import authProvider from './authProvider';

import {
  UserList, UserEdit, UserCreate,
  AuthorList, AuthorEdit, AuthorCreate,
  BookList, BookEdit, BookCreate,
  ReviewList, ReviewEdit, ReviewCreate,
} from './Models';

const httpClient = (url: string, options: Record<string, any> = {}) => {
  if (!options.headers) {
    options.headers = new Headers({ Accept: 'application/json' });
  }
  const token = localStorage.getItem('token');
  options.headers.set('Authorization', `Bearer ${token}`);
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider('api/v1', httpClient);

export const Admin: React.FC = () => {
  return (
    <ReactAdmin dataProvider={dataProvider} authProvider={authProvider}>
      <Resource name="users" list={UserList} edit={UserEdit} create={UserCreate} />
      <Resource name="authors" list={AuthorList} edit={AuthorEdit} create={AuthorCreate} />
      <Resource name="books" list={BookList} edit={BookEdit} create={BookCreate} />
      <Resource name="reviews" list={ReviewList} edit={ReviewEdit} create={ReviewCreate} />
    </ReactAdmin>
  );
};
