#pragma once


#include <mutex>
#include <condition_variable>
#include <thread>
#include <queue>

template <typename T>
class ThreadSafeQueue {
    explicit ThreadSafeQueue(size_t capacity) :
        mCapacity(capacity), mIsRuning(true) {};

    //禁止拷贝和移动
    ThreadSafeQueue(ThreadSafeQueue& other) = delete;
    ThreadSafeQueue& operator=(ThreadSafeQueue& other) = delete;
    ThreadSafeQueue(ThreadSafeQueue&& other) = delete;
    ThreadSafeQueue& operator=(ThreadSafeQueue&& other) = delete;

    //入队
    //出队
    //关闭队列



private:
    std::queue<T> mQueue; //队列
    size_t mCapacity; //容量
    bool mIsRuning;  //是否在运行
    std::mutex mMtx; //锁
    std::condition_variable mCv; //条件变量
};
