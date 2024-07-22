
import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

const validateToken = (req: Request, res: Response, next: NextFunction) => {
    // Excepciones
    if (req.path === '/api/v1/user/signin' || 
        req.path === '/api/v1/user/signup') {
        return next();
    }

    const token = req.headers['authorization']?.split(' ')[1];

    if (!token) {
        return res.status(401).json({ message: 'Access token is missing' });
    }

    jwt.verify(token, JWT_SECRET, (err, decoded) => {
        if (err) {
            return res.status(401).json({ message: 'Invalid or expired token' });
        }
        req.user = decoded;
        next();
    });
};

export { validateToken };
