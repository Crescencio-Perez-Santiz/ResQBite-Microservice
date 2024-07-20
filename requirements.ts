// requirements.ts

// AWS SDK for S3
import { S3Client } from '@aws-sdk/client-s3';

// Environment variable management
import dotenv from 'dotenv';

// Express framework and middleware
import express, { Request, Response, Router, Application } from 'express';
import morgan from 'morgan';
import expressHttpProxy from 'express-http-proxy';

// File system utilities
import fs from 'fs';

// MongoDB and Mongoose for database management
import mongoose from 'mongoose';
import { MongoClient } from 'mongodb';

// Multer for file uploads and Multer-S3 for S3 integration
import multer from 'multer';
import multerS3 from 'multer-s3';

// MySQL and Sequelize for relational database management
import mysql from 'mysql';
import mysql2 from 'mysql2';
import { Sequelize, Model, DataTypes } from 'sequelize';

// AMQP for RabbitMQ integration
import amqp from 'amqplib';
import { connect as amqpConnect } from 'amqp-connection-manager';

// UUID for generating unique identifiers
import { v4 as uuidv4 } from 'uuid';

// Logger
import signale from 'signale';

// Testing libraries
import supertest from 'supertest';
import jest from 'jest';

// TypeScript utilities
import 'ts-node';
import 'ts-node-dev';

console.log('All dependencies imported successfully');
