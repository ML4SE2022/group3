import com.github.mike10004.common.system.SystemInfo;
import com.github.mike10004.common.system.SystemInfo.CpuUsage;
import com.github.mike10004.common.system.SystemInfo.MemoryUsage;

SystemInfo systemInfo = SystemInfo.getInstance();
CpuUsage cpuUsage = systemInfo.getCpuUsage();
MemoryUsage memoryUsage = systemInfo.getMemoryUsage();