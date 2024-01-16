#pragma once

#include <iomanip>
#include <iostream>
#include <vector>

template<typename T>
class Matrix {

    private:

        unsigned int rows;
        unsigned int cols;
        std::vector<std::vector<T>> matrix;

    public:

        Matrix();
        Matrix(unsigned int, unsigned int);
        T &operator() (unsigned int, unsigned int);

        Matrix<T> operator+(Matrix<T> m);
        Matrix<T> operator-(Matrix<T> m);
        Matrix<T> operator*(Matrix<T> m);

        template<typename U>friend std::ostream &operator<<(std::ostream &, const Matrix<U> &);

        void setElem(unsigned int, unsigned int, T);

};


template<typename T>
Matrix<T>::Matrix() : Matrix(1, 1) {}

template<typename T>
Matrix<T>::Matrix(unsigned int rows, unsigned int cols) {

    this->rows = rows;
    this->cols = cols;

    int i, j;

    std::vector<T> temp;

    for (i=0; i<cols; i++) {
        temp.push_back(0);
    }

    for (j=0; j<rows; j++) {
        this->matrix.push_back(temp);
    }

}

template<typename T>
T&Matrix<T>::operator() (unsigned int i, unsigned int j) {
    return (this->matrix)[i-1][j-1];
}

template<typename T>
Matrix<T> Matrix<T>::operator+(Matrix<T> m) {

    Matrix<T> m_new(this->rows, this->cols);

    if (!(this->rows == m.rows) || !(this->cols == m.cols)) {
        std::cout << "1" << std::endl;
        return m_new;
    }

    int i, j;
    T value;

    for (i = 0; i < this->cols; i++){
        for (j = 0; j < this->rows; j++) {
            value = this->matrix[j][i] + m(j+1, i+1);
            m_new.setElem(j+1, i+1, value);
        }
    }

    return m_new;

}

template<typename T>
Matrix<T> Matrix<T>::operator-(Matrix<T> m) {

    Matrix<T> m_new(this->rows, this->cols);

    if (!(this->rows == m.rows) || !(this->cols == m.cols)) {
        return m_new;
    }

    int i, j;
    T value;

    for (i = 0; i < this->cols; i++){
        for (j = 0; j < this->rows; j++) {
            value = this->matrix[j][i] - m(j+1, i+1);
            m_new.setElem(j+1, i+1, value);
        }
    }

    return m_new;

}

template<typename T>
Matrix<T> Matrix<T>::operator*(Matrix<T> m) {

    Matrix<T> m_new(this->rows, m.cols);

    if (!(this->cols == m.rows)) {
        std::cout << "ERROR" << std::endl;
        return m_new;
    }

    int i, j, k;

    for (i = 0; i < this->rows; i++) {
        for (j = 0; j < m.cols; j++) {
            for (k = 0; k < m.rows; k++) {
                m_new.setElem(i+1, j+1, m_new(i+1, j+1) + (this->matrix[i][k] * m(k+1, j+1)));
            }
        }
    }

    return m_new;

}

template<typename U>
std::ostream &operator<<(std::ostream &os, const Matrix<U> &m) {

    int i;
    int j;

    for (i = 0; i < m.rows; i++) {
        for (j = 0; j < m.cols; j++) {
            os << std::setfill(' ') << std::setw(2) << m.matrix[i][j] << ' ';
        }
        os << '\n';
    }

    return os;

}

template<typename T>
void Matrix<T>::setElem(unsigned int row, unsigned int col, T value) {

    this->matrix[row-1][col-1] = value;

}