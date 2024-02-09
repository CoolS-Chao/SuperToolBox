#include <cstdio>
#include <string>
#include <iostream>
#include <cstring>
#include <ctime>

#define LOG_FILE "log.txt"

//void logMessage(const char *message) {
void logMessage(const std::string& message) {
    time_t currentTime;
    time(&currentTime);

    char *timeString = ctime(&currentTime);
    FILE *file = fopen(LOG_FILE, "a");
    if (file != NULL) {
        fprintf(file, "[%s] %s\n", timeString, message.c_str());
        fclose(file);
    } else {
        printf("Error opening log file: %s\n", LOG_FILE);
    }
}

int main() {
    bool bIpChange;
    char cmd[256];
    std::string name = "eth2";
    sprintf(cmd, "busybox ifconfig %s", name.c_str());
    FILE* fp = NULL;
    fp = popen(cmd, "r");

    std::cout << 111 << std::endl;
    
    if (fp)
    {
        char output[1024];
        unsigned int rxByte = 0, txByte = 0;
        //uint rxByte = 0, txByte = 0;
        while (fgets(output, 1024, fp) != NULL)
        {
            char* p = NULL;
            p = strstr(output, "HWaddr");
            if (p)
            {
                char* pEnd = strchr(p, '\r');
                if (pEnd == NULL)
                {
                    pEnd = strchr(p, '\n');
                }
                p += strlen("HWaddr ");
                if (pEnd)
                {
                    std::string mac;
                    mac = std::string(p, pEnd - p);
                }
            }
            p = strstr(output, "inet addr:");
            if (p)
            {
                p += strlen("inet addr:");
                char* pEnd = strchr(p, ' ');
                if (pEnd)
                {
                    std::string ip;
                    if (ip != std::string(p, pEnd - p))
                    {
                        ip = std::string(p, pEnd - p);
                        logMessage(ip);
                        bIpChange = true;
                    }
                }
            }
            p = strstr(output, "Mask:");
            if (p)
            {
                char* pEnd = strchr(p, '\r');
                if (pEnd == NULL)
                {
                    std::string pEnd;
                    pEnd = strchr(p, '\n');
                }
                p += strlen("Mask:");
                if (pEnd)
                {
                    std::string mask;
                    mask = std::string(p, pEnd - p);
                }
            }
            p = strstr(output, "RX bytes:");
            if (p)
            {
                p += strlen("RX bytes:");
                char* pEnd = strchr(p, ' ');
                if (pEnd)
                {
                    rxByte = atoi(std::string(p, pEnd - p).c_str());
                }
            }
            p = strstr(output, "TX bytes:");
            if (p)
            {
                p += strlen("TX bytes:");
                char* pEnd = strchr(p, ' ');
                if (pEnd)
                {
                    txByte = atoi(std::string(p, pEnd - p).c_str());
                }
            }
        }
    }
    else
    {
        logMessage("Nt fp");
    }
    return 0;
}